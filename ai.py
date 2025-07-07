Fait sans emoji est avec ce modem : # Load model directly
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained("TheBloke/WizardLM-Uncensored-Falcon-7B-GPTQ", trust_remote_code=True) ou # Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="TheBloke/WizardLM-Uncensored-Falcon-7B-GPTQ", trust_remote_code=True)
