# Generative AI Master Projects

Complete master's level coursework on Generative AI, LLM Alignment, and Deep Learning (HAW Kiel, 2025)

## 🎯 Project Overview

This repository contains comprehensive hands-on implementations covering:
- **AI Alignment & Safety**: Multi-agent debate systems, reward misgeneralization
- **Generative Models**: Stable Diffusion, text-to-image pipelines, GANs
- **Deep Learning Fundamentals**: Neural networks, CNNs, RNNs, transformers
- **Parameter-Efficient Methods**: LoRA, PEFT, transfer learning
- **Practical Integration**: LMStudio, Hugging Face, PyTorch

## 📚 All Sessions (0-11)

### Session 2: Deep Learning Foundations
Core neural network concepts and implementations
- Feedforward networks, backpropagation
- Activation functions, optimizers
- Training strategies and regularization

### Session 3: Advanced Neural Architectures
Convolutional and recurrent networks
- CNNs for computer vision
- RNNs and LSTMs for sequences
- Attention mechanisms

### Session 4: Transformers & NLP
Modern transformer architectures
- Self-attention and multi-head attention
- BERT, GPT foundations
- Fine-tuning for NLP tasks

### [Session 8: Stable Diffusion](Session-8-StableDiffusion/)
Text-to-image generation with detailed architecture exploration
- Stable Diffusion v1.5 pipeline implementation
- Parameter experiments (guidance scale, inference steps, seeds)
- Architecture inspection (CLIP, UNet, VAE components)
- Prompt engineering techniques

### [Session 9: Advanced Image Generation](Session-9-ImageGeneration/)
Beyond text-to-image: advanced diffusion techniques
- Image-to-Image pipelines (strength parameter tuning)
- Inpainting and region-based editing
- Negative prompts for quality control
- Pipeline comparison (Text2Img, Img2Img, Inpaint, ControlNet)

### [Session 10: Parameter-Efficient Finetuning](Session-10-Finetuning/)
Adapting large models with minimal resources
- Transfer learning foundations
- LoRA (Low-Rank Adaptation) implementation
- PEFT methods comparison (99% parameter reduction)
- Training strategies and evaluation metrics

### [Session 11: Alignment Challenge](Session-11-Alignment-LMStudio/) ⭐
**Featured Project**: Multi-agent debate for improved reasoning
- **Problem**: Reward misgeneralization and hacking (Casper et al. 2023)
- **Solution**: 3-round multi-agent debate system
- **Implementation**: LMStudio integration with llama-3.2-instruct
- **Results**: Demonstrable reasoning improvement across puzzle/math questions

## 🔑 Key Concepts

✅ **Reward Misgeneralization**: Models learn shortcuts correlated with training rewards but fail on new situations  
✅ **Multi-Agent Debate**: Iterative reasoning refinement through adversarial agents  
✅ **Latent Diffusion**: Efficient image generation via compressed latent space (512×512 → 64×64)  
✅ **LoRA Adaptation**: Fine-tune billion-parameter models with <1% trainable parameters  
✅ **Transformer Architecture**: Self-attention mechanisms for sequence modeling  
✅ **LMStudio Integration**: Local LLM deployment with OpenAI-compatible APIs  

## 🛠️ Technologies

- **Python 3.10+**: Core language
- **PyTorch 2.0+**: Deep learning framework
- **Hugging Face Ecosystem**: Transformers, Diffusers, PEFT
- **LMStudio**: Local LLM serving (http://localhost:1234/v1)
- **Jupyter Notebooks**: Interactive development

## 🚀 Quick Start

### Prerequisites
```bash
# Install Python dependencies
pip install -r requirements.txt

# Install LMStudio (for Session 11)
# Download from: https://lmstudio.ai
```

### Running Session 11 (Multi-Agent Debate) ⭐ FLAGSHIP
```bash
# 1. Start LMStudio
# 2. Load llama-3.2-instruct (or compatible chat model)
# 3. Start server at http://localhost:1234/v1

# 4. Run notebook
cd Session-11-Alignment-LMStudio/
jupyter notebook Session11_Alignment_LMStudio.ipynb
```

### Running Sessions 8-10 (Diffusion & Finetuning)
```bash
# Recommended: Run on Google Colab (free GPU)
# Or locally with CUDA-enabled GPU (8GB+ VRAM)

jupyter notebook Session-8-StableDiffusion/Session8_StableDiffusion.ipynb
```

### Running Sessions 2-4 (Foundations)
```bash
jupyter notebook Session-2/session2.ipynb
```

## 📊 Expected Results

**Sessions 2-4**: Neural network training curves, classification results, attention visualizations  
**Session 8**: Generated images from text prompts, parameter sensitivity analysis  
**Session 9**: Style transfer examples, inpainting demonstrations  
**Session 10**: LoRA-finetuned model with 99% fewer parameters  
**Session 11**: Multi-agent debate transcripts showing reasoning convergence  

## 🎓 Academic Context

Master's Coursework in Computer Science (HAW Kiel, 2025)  
Focus Areas: Generative AI, LLM Safety, Deep Learning, Computer Vision

**Key References**:  
- Casper et al. (2023) - "Open Problems and Fundamental Limitations of RLHF"
- Rombach et al. (2022) - "High-Resolution Image Synthesis with Latent Diffusion Models"
- Hu et al. (2021) - "LoRA: Low-Rank Adaptation of Large Language Models"

## 👤 Author

**Rakesh Reddy**  
Master's in Computer Science, HAW Kiel  
GitHub: [@RakeshReddy26-bit](https://github.com/RakeshReddy26-bit)  
Repository: [generative-ai-master-projects](https://github.com/RakeshReddy26-bit/generative-ai-master-projects)

## 📄 License

MIT License - See LICENSE file for details

---

## 💼 For Recruiters

This repository demonstrates:
- **End-to-end ML expertise**: From neural network fundamentals to cutting-edge generative AI
- **Research Implementation**: Reading academic papers → working code (Casper, Rombach, Hu et al.)
- **System Integration**: LMStudio, Hugging Face, PyTorch ecosystem
- **Problem-Solving**: Multi-agent debate for alignment challenges
- **Technical Depth**: Diffusion architecture, LoRA mathematics, transformer mechanics
- **Production-Ready Code**: Professional documentation, reproducible notebooks

**Highlighted Skills**:
- 🎯 AI Safety & Alignment (Session 11)
- 🎨 Generative AI (Stable Diffusion, Sessions 8-9)
- ⚡ Efficient ML (LoRA/PEFT, Session 10)
- 🧠 Deep Learning Foundations (Sessions 2-4)

**Live Demo Available**: Contact for Session 11 multi-agent debate demonstration

---

**Total Sessions**: 12 (Sessions 0-11)  
**Lines of Code**: 2000+  
**Technologies**: PyTorch, Transformers, Diffusers, PEFT, LMStudio  
**Status**: ✅ All sessions complete and tested
