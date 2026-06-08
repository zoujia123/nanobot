# Relevance Rules

Use these rules after fetching arXiv metadata. Judge by title and abstract, not by keywords alone.

## Relevant

A paper is relevant when it studies systems-level methods for large models, including:

- LLM serving, online inference, offline inference, or batch inference
- Prefill/decode scheduling, batching, request routing, SLO/QoS control, or load balancing
- KV cache management, prefix caching, cache reuse, cache compression, or offloading
- Speculative decoding, structured decoding systems, or inference runtime optimization
- Quantization, sparsity, CUDA/kernel/operator optimization, compiler/runtime support
- Distributed training, RLHF/post-training systems, checkpointing, parallelism, or resource scheduling
- MoE serving/training systems, expert placement, communication optimization
- Edge/mobile LLM inference, networking, hardware, storage, or disaggregation for large models
- RAG systems only when the focus is retrieval infrastructure, efficiency, indexing, scheduling, or serving

## Not Relevant

Exclude papers when they:

- Only use LLMs as an application tool
- Focus mainly on model capability, benchmark scores, prompting, alignment, safety, or evaluation
- Are about security, interpretability, privacy, or federated learning without a large-model systems contribution
- Study traditional distributed systems or traditional ML systems without clear large-model relevance
- Mention LLMs only as motivation but do not optimize training, inference, serving, or infrastructure

## Borderline Rule

When uncertain, include the paper only if the abstract clearly states:

1. A systems bottleneck or resource problem
2. A concrete system, runtime, algorithm, kernel, scheduler, or infrastructure design
3. A measurable systems result such as latency, throughput, memory, cost, utilization, or scalability
