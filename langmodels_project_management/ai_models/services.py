from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from accelerate.test_utils.testing import get_backend

class BaseModel:
    def __init__(self, model_identifier):
        self.model_identifier = model_identifier

        self.tokenizer = AutoTokenizer.from_pretrained(model_identifier)
        self.tokenizer.pad_token = self.tokenizer.eos_token

        quantization_config = BitsAndBytesConfig(load_in_8bit=True)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_identifier, 
            device_map="auto", 
            quantization_config=quantization_config
        )

        self.DEVICE, _, _ = get_backend()

    def generate_text(self, prompt):
        model_inputs = self.tokenizer(
            [prompt],
            return_tensors="pt"
        ).to(self.DEVICE)

        generated_ids = self.model.generate(
            **model_inputs, 
            do_sample=True,
            min_new_tokens=50, # 200
            max_new_tokens=150 # 500
            # max_time=float  
        )

        return (self.tokenizer.batch_decode(
            generated_ids, 
            skip_special_tokens=True
            )[0])