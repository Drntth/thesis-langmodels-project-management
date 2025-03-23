from transformers import set_seed
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from accelerate.test_utils.testing import get_backend


class TokenizerModel:
    def __init__(self, model_identifier):
        self.model_identifier = model_identifier

        self.tokenizer = AutoTokenizer.from_pretrained(model_identifier)
        self.tokenizer.pad_token = self.tokenizer.eos_token

        quantization_config = BitsAndBytesConfig(load_in_8bit=True)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_identifier, device_map="auto", quantization_config=quantization_config
        )

        self.DEVICE, _, _ = get_backend()

    def generate_text(self, prompt, min_new_tokens=50, max_new_tokens=150):
        model_inputs = self.tokenizer([prompt], return_tensors="pt").to(self.DEVICE)

        generated_ids = self.model.generate(
            **model_inputs,
            do_sample=True,
            min_new_tokens=min_new_tokens,
            max_new_tokens=max_new_tokens,
        )

        output_text = self.tokenizer.batch_decode(
            generated_ids, skip_special_tokens=True
        )[0]

        return output_text


model_identifiers = [
    "distilbert/distilgpt2",
    "EleutherAI/gpt-neo-125m",
    "facebook/opt-125m",
    "openai-community/gpt2-medium",
    "facebook/opt-350m",
]

prompt = "Generate a comprehensive specification document for a mobile app development project. Describe the app's features, target audience, technical requirements, design guidelines, testing strategies, and launch plan."
set_seed(0)

for model_id in model_identifiers:
    print(f"\n\n{model_id}:")

    ai_model_instance = TokenizerModel(model_id)
    generated_text = ai_model_instance.generate_text(
        prompt,
        min_tokens=20,  # 50, 100
        max_tokens=50,  # 150, 300
    )

    print(generated_text)
    print("-" * 80)
