from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from transformers import pipeline
from accelerate.test_utils.testing import get_backend


class PipelineTextGenerator:
    def __init__(self, model_identifier):
        self.model_identifier = model_identifier
        self.generator = pipeline("text-generation", model=self.model_identifier)

    def generate_text(self, prompt, min_new_tokens=50, max_new_tokens=150):
        output_text = self.generator(
            prompt,
            do_sample=True,
            min_new_tokens=min_new_tokens,
            max_new_tokens=max_new_tokens,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            temperature=0.3,
            top_p=0.9,
            repetition_penalty=1.2,
            truncation=True,
            return_full_text=False,
            pad_token_id=self.generator.model.config.eos_token_id,
        )[0]["generated_text"]

        return output_text


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
