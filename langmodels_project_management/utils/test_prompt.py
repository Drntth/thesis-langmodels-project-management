from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, set_seed
from accelerate.test_utils.testing import get_backend

model_identifier = "distilbert/distilgpt2"

tokenizer = AutoTokenizer.from_pretrained(model_identifier)
tokenizer.pad_token = tokenizer.eos_token

quantization_config = BitsAndBytesConfig(load_in_8bit=True)
model = AutoModelForCausalLM.from_pretrained(
    model_identifier, 
    device_map="auto", 
    quantization_config=quantization_config
)

DEVICE, _, _ = get_backend()
set_seed(0)
prompt = """I'm a cat"""
model_inputs = tokenizer(
    [prompt],
    return_tensors="pt"
).to(DEVICE)
input_length = model_inputs.input_ids.shape[1]

generated_ids = model.generate(
    **model_inputs, 
    do_sample=True,
    min_new_tokens=50, # 200
    max_new_tokens=150 # 500
    # max_time=float  
)

print(tokenizer.batch_decode(
    generated_ids, 
    skip_special_tokens=True
    )[0])