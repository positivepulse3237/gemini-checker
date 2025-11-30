import google.generativeai as genai
import os

# Get API key from environment
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("BRUTAL TRUTH: GEMINI_API_KEY is missing from secrets.")
    exit(1)

# Configure the library
genai.configure(api_key=api_key)

print("--- CHECKING AVAILABLE GEMINI MODELS ---")

try:
    # List all models available to your API key
    models = genai.list_models()
    found_any = False
    
    for m in models:
        # We only care about models that can generate text/content
        if 'generateContent' in m.supported_generation_methods:
            print(f"AVAILABLE: {m.name} (Version: {m.version})")
            found_any = True
            
    if not found_any:
        print("BRUTAL TRUTH: No models found that support 'generateContent'.")
        
except Exception as e:
    print(f"BRUTAL ERROR: Could not list models. Reason: {e}")

print("--- END OF CHECK ---")
