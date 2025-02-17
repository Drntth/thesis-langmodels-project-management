from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from huggingface_hub import snapshot_download

class BaseModel:
    def __init__(self, model_identifier):
        self.model_identifier = model_identifier

        self.pipeline = pipeline(
            "text-generation", 
            model=self.model_identifier, 
        )

    def generate_text(self, prompt):
        return self.pipeline(
            prompt,
            # max_length=100, # a teljes generált szöveg hossza: input + output
            # max_new_tokens=50, # generált új tokenek száma
            # do_sample=True, # véletlenszerű mintavételezés 
            # temperature=0.7, # kreativitás 0-1
            # repetition_penalty=1.5, # Ismétlődés büntetése (1.0 = nincs büntetés, >1.0 = ismétlődés elkerülése)
            num_return_sequences=1, # válaszok száma
            return_full_text=False, # prompt + generált szöveg
        )[0]["generated_text"]