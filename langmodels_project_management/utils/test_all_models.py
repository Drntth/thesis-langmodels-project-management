from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, set_seed
from accelerate.test_utils.testing import get_backend

model_identifiers = [
    "distilbert/distilgpt2",
    "EleutherAI/gpt-neo-125m",
    "facebook/opt-125m",
    "openai-community/gpt2-medium",
    "facebook/opt-350m"
]

quantization_config = BitsAndBytesConfig(load_in_8bit=True)
prompt = "Generate a comprehensive specification document for a mobile app development project. Describe the app's features, target audience, technical requirements, design guidelines, testing strategies, and launch plan."
set_seed(0)
DEVICE, _, _ = get_backend()

for model_id in model_identifiers:
    print(f"\n\n{model_id}:")

    tokenizer = AutoTokenizer.from_pretrained(model_id)
    tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        model_id, 
        device_map="auto", 
        quantization_config=quantization_config
    )

    model_inputs = tokenizer([prompt], return_tensors="pt").to(DEVICE)

    generated_ids = model.generate(
        **model_inputs, 
        do_sample=True,
        min_new_tokens=50, # 200
        max_new_tokens=150 # 500
    )

    generated_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    print(generated_text)
    print("-" * 80)
