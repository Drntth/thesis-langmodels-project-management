from transformers import set_seed
from transformers import pipeline


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

    ai_model_instance = PipelineTextGenerator(model_id)
    generated_text = ai_model_instance.generate_text(
        prompt,
        # min_tokens=20, # 50, 100
        # max_tokens=50 # 150, 300
    )

    print(generated_text)
    print("-" * 80)
