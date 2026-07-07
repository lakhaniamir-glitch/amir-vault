# beta-design Cumulative Learnings


## 2026-07-07
### Actionable
- [Start building with Nano Banana 2 Lite and Gemini Omni Flash](https://deepmind.google/blog/start-building-with-nano-banana-2-lite-and-gemini-omni-flash/) - This is a direct update to the "nano-banana" image generation model family Aydins uses for product hero shots, potentially offering better quality or lower cost. **Action:** Test Nano Banana 2 Lite against the current reference image rule (2026-06-04) to see if it improves product visuals or reduces inference costs.
- [Introducing computer use in Gemini 3.5 Flash](https://deepmind.google/blog/introducing-computer-use-in-gemini-3-5-flash/) - This adds agentic UI interaction capabilities to a fast, cheap model, which could enhance or replace parts of the current agentic loops on the Hetzner VPS. **Action:** Evaluate if Gemini 3.5 Flash with computer use can perform tasks currently handled by the beta orchestrator or channel specialists more efficiently.
- [Run a vLLM Server on HF Jobs in One Command](https://huggingface.co/blog/vllm-jobs) - This simplifies deploying high-performance LLM inference, which could be an alternative to the current OpenRouter/DeepSeek setup for cheaper or more controlled synthesis. **Action:** Test running a cost-effective model (e.g., a Gemma variant) on Hugging Face Jobs to compare latency and cost against OpenRouter for synthesis tasks.
