# 🧪 Lab 1 — Generative Models: GAN vs VAE - Complete Experiment Report

**Generated:** 2025-12-02 14:03:06

---

## Experiment Summary

- **Datasets:** MNIST, FashionMNIST
- **Total GAN Experiments:** 12
- **Total VAE Experiments:** 6
- **Epochs per Experiment:** 10

---

## Part 1: GAN Experiments - MNIST

### Experiment Configurations
- **Loss Types:** Hinge, BCE
- **Z Dimensions:** 64, 32, 128
- **Total Experiments:** 6

### Results Summary

#### MNIST_GAN_hinge_z64
- **Loss Type:** hinge
- **Z Dimension:** 64
- **Best Epoch:** 10
- **Final D Loss:** 1.2151
- **Final G Loss:** 0.6088
- **Proxy FID Score:** 0.05

**Sample Images (Epoch 10):**

<img src="gan_samples/MNIST_GAN_hinge_z64_epoch10.png" width="300">

#### MNIST_GAN_hinge_z32
- **Loss Type:** hinge
- **Z Dimension:** 32
- **Best Epoch:** 10
- **Final D Loss:** 1.2959
- **Final G Loss:** 0.5416
- **Proxy FID Score:** 0.03

**Sample Images (Epoch 10):**

<img src="gan_samples/MNIST_GAN_hinge_z32_epoch10.png" width="300">

#### MNIST_GAN_hinge_z128
- **Loss Type:** hinge
- **Z Dimension:** 128
- **Best Epoch:** 10
- **Final D Loss:** 1.1298
- **Final G Loss:** 0.6788
- **Proxy FID Score:** 0.04

**Sample Images (Epoch 10):**

<img src="gan_samples/MNIST_GAN_hinge_z128_epoch10.png" width="300">

#### MNIST_GAN_bce_z64
- **Loss Type:** bce
- **Z Dimension:** 64
- **Best Epoch:** 10
- **Final D Loss:** 1.0181
- **Final G Loss:** 1.2392
- **Proxy FID Score:** 0.05

**Sample Images (Epoch 10):**

<img src="gan_samples/MNIST_GAN_bce_z64_epoch10.png" width="300">

#### MNIST_GAN_bce_z32
- **Loss Type:** bce
- **Z Dimension:** 32
- **Best Epoch:** 10
- **Final D Loss:** 1.0849
- **Final G Loss:** 1.1143
- **Proxy FID Score:** 0.04

**Sample Images (Epoch 10):**

<img src="gan_samples/MNIST_GAN_bce_z32_epoch10.png" width="300">

#### MNIST_GAN_bce_z128
- **Loss Type:** bce
- **Z Dimension:** 128
- **Best Epoch:** 10
- **Final D Loss:** 0.9333
- **Final G Loss:** 1.4068
- **Proxy FID Score:** 0.06

**Sample Images (Epoch 10):**

<img src="gan_samples/MNIST_GAN_bce_z128_epoch10.png" width="300">

## Part 1: GAN Experiments - FashionMNIST

### Experiment Configurations
- **Loss Types:** Hinge, BCE
- **Z Dimensions:** 64, 32, 128
- **Total Experiments:** 6

### Results Summary

#### FashionMNIST_GAN_hinge_z64
- **Loss Type:** hinge
- **Z Dimension:** 64
- **Best Epoch:** 10
- **Final D Loss:** 1.3945
- **Final G Loss:** 0.4709
- **Proxy FID Score:** 0.06

**Sample Images (Epoch 10):**

<img src="gan_samples/FashionMNIST_GAN_hinge_z64_epoch10.png" width="300">

#### FashionMNIST_GAN_hinge_z32
- **Loss Type:** hinge
- **Z Dimension:** 32
- **Best Epoch:** 10
- **Final D Loss:** 1.4563
- **Final G Loss:** 0.4275
- **Proxy FID Score:** 0.07

**Sample Images (Epoch 10):**

<img src="gan_samples/FashionMNIST_GAN_hinge_z32_epoch10.png" width="300">

#### FashionMNIST_GAN_hinge_z128
- **Loss Type:** hinge
- **Z Dimension:** 128
- **Best Epoch:** 10
- **Final D Loss:** 1.3273
- **Final G Loss:** 0.5369
- **Proxy FID Score:** 0.06

**Sample Images (Epoch 10):**

<img src="gan_samples/FashionMNIST_GAN_hinge_z128_epoch10.png" width="300">

#### FashionMNIST_GAN_bce_z64
- **Loss Type:** bce
- **Z Dimension:** 64
- **Best Epoch:** 10
- **Final D Loss:** 1.1371
- **Final G Loss:** 1.0390
- **Proxy FID Score:** 0.08

**Sample Images (Epoch 10):**

<img src="gan_samples/FashionMNIST_GAN_bce_z64_epoch10.png" width="300">

#### FashionMNIST_GAN_bce_z32
- **Loss Type:** bce
- **Z Dimension:** 32
- **Best Epoch:** 10
- **Final D Loss:** 1.1543
- **Final G Loss:** 1.0175
- **Proxy FID Score:** 0.09

**Sample Images (Epoch 10):**

<img src="gan_samples/FashionMNIST_GAN_bce_z32_epoch10.png" width="300">

#### FashionMNIST_GAN_bce_z128
- **Loss Type:** bce
- **Z Dimension:** 128
- **Best Epoch:** 10
- **Final D Loss:** 1.0529
- **Final G Loss:** 1.1701
- **Proxy FID Score:** 0.08

**Sample Images (Epoch 10):**

<img src="gan_samples/FashionMNIST_GAN_bce_z128_epoch10.png" width="300">

## Part 2: VAE Experiments - MNIST

### Experiment Configurations
- **Latent Dimensions:** 16, 8, 32
- **Total Experiments:** 3

### Results Summary

#### MNIST_VAE_latent16
- **Latent Dimension:** 16
- **Best Epoch:** 10
- **Final Total Loss:** 78.1758
- **Final Recon Loss:** 52.8648
- **Final KL Loss:** 25.3110
- **Proxy FID Score:** 0.33

**Reconstruction (Epoch 10):**

<img src="vae_reconstructions/MNIST_VAE_latent16_epoch10.png" width="300">

**Random Samples:**

<img src="vae_samples/MNIST_VAE_latent16_random.png" width="300">

**Latent Interpolation:**

<img src="vae_interpolations/MNIST_VAE_latent16_interpolation.png" width="300">

#### MNIST_VAE_latent8
- **Latent Dimension:** 8
- **Best Epoch:** 10
- **Final Total Loss:** 86.7948
- **Final Recon Loss:** 69.3989
- **Final KL Loss:** 17.3960
- **Proxy FID Score:** 0.25

**Reconstruction (Epoch 10):**

<img src="vae_reconstructions/MNIST_VAE_latent8_epoch10.png" width="300">

**Random Samples:**

<img src="vae_samples/MNIST_VAE_latent8_random.png" width="300">

**Latent Interpolation:**

<img src="vae_interpolations/MNIST_VAE_latent8_interpolation.png" width="300">

#### MNIST_VAE_latent32
- **Latent Dimension:** 32
- **Best Epoch:** 10
- **Final Total Loss:** 78.1761
- **Final Recon Loss:** 49.4401
- **Final KL Loss:** 28.7360
- **Proxy FID Score:** 0.40

**Reconstruction (Epoch 10):**

<img src="vae_reconstructions/MNIST_VAE_latent32_epoch10.png" width="300">

**Random Samples:**

<img src="vae_samples/MNIST_VAE_latent32_random.png" width="300">

**Latent Interpolation:**

<img src="vae_interpolations/MNIST_VAE_latent32_interpolation.png" width="300">

## Part 2: VAE Experiments - FashionMNIST

### Experiment Configurations
- **Latent Dimensions:** 16, 8, 32
- **Total Experiments:** 3

### Results Summary

#### FashionMNIST_VAE_latent16
- **Latent Dimension:** 16
- **Best Epoch:** 10
- **Final Total Loss:** 108.4302
- **Final Recon Loss:** 86.0348
- **Final KL Loss:** 22.3954
- **Proxy FID Score:** 0.94

**Reconstruction (Epoch 10):**

<img src="vae_reconstructions/FashionMNIST_VAE_latent16_epoch10.png" width="300">

**Random Samples:**

<img src="vae_samples/FashionMNIST_VAE_latent16_random.png" width="300">

**Latent Interpolation:**

<img src="vae_interpolations/FashionMNIST_VAE_latent16_interpolation.png" width="300">

#### FashionMNIST_VAE_latent8
- **Latent Dimension:** 8
- **Best Epoch:** 10
- **Final Total Loss:** 110.3554
- **Final Recon Loss:** 93.0578
- **Final KL Loss:** 17.2976
- **Proxy FID Score:** 0.78

**Reconstruction (Epoch 10):**

<img src="vae_reconstructions/FashionMNIST_VAE_latent8_epoch10.png" width="300">

**Random Samples:**

<img src="vae_samples/FashionMNIST_VAE_latent8_random.png" width="300">

**Latent Interpolation:**

<img src="vae_interpolations/FashionMNIST_VAE_latent8_interpolation.png" width="300">

#### FashionMNIST_VAE_latent32
- **Latent Dimension:** 32
- **Best Epoch:** 10
- **Final Total Loss:** 114.6294
- **Final Recon Loss:** 92.4168
- **Final KL Loss:** 22.2125
- **Proxy FID Score:** 0.93

**Reconstruction (Epoch 10):**

<img src="vae_reconstructions/FashionMNIST_VAE_latent32_epoch10.png" width="300">

**Random Samples:**

<img src="vae_samples/FashionMNIST_VAE_latent32_random.png" width="300">

**Latent Interpolation:**

<img src="vae_interpolations/FashionMNIST_VAE_latent32_interpolation.png" width="300">

## Generated Images

All generated images are saved in the `results/` directory. Key images are embedded below:

### GAN Generated Samples (Best Epoch)

#### MNIST

**MNIST_GAN_hinge_z64** (Epoch 10):

![MNIST_GAN_hinge_z64](gan_samples/MNIST_GAN_hinge_z64_epoch10.png)

**MNIST_GAN_hinge_z32** (Epoch 10):

![MNIST_GAN_hinge_z32](gan_samples/MNIST_GAN_hinge_z32_epoch10.png)

**MNIST_GAN_hinge_z128** (Epoch 10):

![MNIST_GAN_hinge_z128](gan_samples/MNIST_GAN_hinge_z128_epoch10.png)

**MNIST_GAN_bce_z64** (Epoch 10):

![MNIST_GAN_bce_z64](gan_samples/MNIST_GAN_bce_z64_epoch10.png)

**MNIST_GAN_bce_z32** (Epoch 10):

![MNIST_GAN_bce_z32](gan_samples/MNIST_GAN_bce_z32_epoch10.png)

**MNIST_GAN_bce_z128** (Epoch 10):

![MNIST_GAN_bce_z128](gan_samples/MNIST_GAN_bce_z128_epoch10.png)

#### FashionMNIST

**FashionMNIST_GAN_hinge_z64** (Epoch 10):

![FashionMNIST_GAN_hinge_z64](gan_samples/FashionMNIST_GAN_hinge_z64_epoch10.png)

**FashionMNIST_GAN_hinge_z32** (Epoch 10):

![FashionMNIST_GAN_hinge_z32](gan_samples/FashionMNIST_GAN_hinge_z32_epoch10.png)

**FashionMNIST_GAN_hinge_z128** (Epoch 10):

![FashionMNIST_GAN_hinge_z128](gan_samples/FashionMNIST_GAN_hinge_z128_epoch10.png)

**FashionMNIST_GAN_bce_z64** (Epoch 10):

![FashionMNIST_GAN_bce_z64](gan_samples/FashionMNIST_GAN_bce_z64_epoch10.png)

**FashionMNIST_GAN_bce_z32** (Epoch 10):

![FashionMNIST_GAN_bce_z32](gan_samples/FashionMNIST_GAN_bce_z32_epoch10.png)

**FashionMNIST_GAN_bce_z128** (Epoch 10):

![FashionMNIST_GAN_bce_z128](gan_samples/FashionMNIST_GAN_bce_z128_epoch10.png)

### VAE Reconstructions (Best Epoch)

#### MNIST

**MNIST_VAE_latent16** (Epoch 10):

![MNIST_VAE_latent16 Reconstructions](vae_reconstructions/MNIST_VAE_latent16_epoch10.png)

**MNIST_VAE_latent8** (Epoch 10):

![MNIST_VAE_latent8 Reconstructions](vae_reconstructions/MNIST_VAE_latent8_epoch10.png)

**MNIST_VAE_latent32** (Epoch 10):

![MNIST_VAE_latent32 Reconstructions](vae_reconstructions/MNIST_VAE_latent32_epoch10.png)

#### FashionMNIST

**FashionMNIST_VAE_latent16** (Epoch 10):

![FashionMNIST_VAE_latent16 Reconstructions](vae_reconstructions/FashionMNIST_VAE_latent16_epoch10.png)

**FashionMNIST_VAE_latent8** (Epoch 10):

![FashionMNIST_VAE_latent8 Reconstructions](vae_reconstructions/FashionMNIST_VAE_latent8_epoch10.png)

**FashionMNIST_VAE_latent32** (Epoch 10):

![FashionMNIST_VAE_latent32 Reconstructions](vae_reconstructions/FashionMNIST_VAE_latent32_epoch10.png)

### VAE Random Samples

#### MNIST

**MNIST_VAE_latent16**:

![MNIST_VAE_latent16 Random Samples](vae_samples/MNIST_VAE_latent16_random.png)

**MNIST_VAE_latent8**:

![MNIST_VAE_latent8 Random Samples](vae_samples/MNIST_VAE_latent8_random.png)

**MNIST_VAE_latent32**:

![MNIST_VAE_latent32 Random Samples](vae_samples/MNIST_VAE_latent32_random.png)

#### FashionMNIST

**FashionMNIST_VAE_latent16**:

![FashionMNIST_VAE_latent16 Random Samples](vae_samples/FashionMNIST_VAE_latent16_random.png)

**FashionMNIST_VAE_latent8**:

![FashionMNIST_VAE_latent8 Random Samples](vae_samples/FashionMNIST_VAE_latent8_random.png)

**FashionMNIST_VAE_latent32**:

![FashionMNIST_VAE_latent32 Random Samples](vae_samples/FashionMNIST_VAE_latent32_random.png)

### VAE Latent Interpolations

#### MNIST

**MNIST_VAE_latent16**:

![MNIST_VAE_latent16 Interpolation](vae_interpolations/MNIST_VAE_latent16_interpolation.png)

**MNIST_VAE_latent8**:

![MNIST_VAE_latent8 Interpolation](vae_interpolations/MNIST_VAE_latent8_interpolation.png)

**MNIST_VAE_latent32**:

![MNIST_VAE_latent32 Interpolation](vae_interpolations/MNIST_VAE_latent32_interpolation.png)

#### FashionMNIST

**FashionMNIST_VAE_latent16**:

![FashionMNIST_VAE_latent16 Interpolation](vae_interpolations/FashionMNIST_VAE_latent16_interpolation.png)

**FashionMNIST_VAE_latent8**:

![FashionMNIST_VAE_latent8 Interpolation](vae_interpolations/FashionMNIST_VAE_latent8_interpolation.png)

**FashionMNIST_VAE_latent32**:

![FashionMNIST_VAE_latent32 Interpolation](vae_interpolations/FashionMNIST_VAE_latent32_interpolation.png)

---

### All Image Files

All generated images are saved in the `results/` directory:

- `gan_samples/` - GAN generated samples for each experiment and epoch
- `vae_reconstructions/` - VAE reconstruction comparisons
- `vae_samples/` - VAE random samples from latent space
- `vae_interpolations/` - VAE latent space interpolations
- `models/` - Saved model checkpoints for FID computation

## Mode Collapse Analysis

> **Note:** You can answer all reflection questions regardless of whether mode collapse occurs.
> - If mode collapse occurs: analyze which configurations caused it and what helped.
> - If mode collapse doesn't occur: note which configurations were stable and why.

### GAN Mode Collapse Summary

- **No mode collapse detected** in any GAN experiments.
- All experiments maintained good diversity throughout training.
- This suggests the hyperparameters (loss type, Z_DIM, learning rate) were well-tuned.

### Stable GAN Configurations (No Mode Collapse)

- **MNIST_GAN_hinge_z64** (Loss: hinge, Z_DIM: 64)
  - Final diversity score: 0.2908
- **MNIST_GAN_hinge_z32** (Loss: hinge, Z_DIM: 32)
  - Final diversity score: 0.3181
- **MNIST_GAN_hinge_z128** (Loss: hinge, Z_DIM: 128)
  - Final diversity score: 0.2985
- **MNIST_GAN_bce_z64** (Loss: bce, Z_DIM: 64)
  - Final diversity score: 0.2993
- **MNIST_GAN_bce_z32** (Loss: bce, Z_DIM: 32)
  - Final diversity score: 0.3056
- **MNIST_GAN_bce_z128** (Loss: bce, Z_DIM: 128)
  - Final diversity score: 0.3160
- **FashionMNIST_GAN_hinge_z64** (Loss: hinge, Z_DIM: 64)
  - Final diversity score: 0.5393
- **FashionMNIST_GAN_hinge_z32** (Loss: hinge, Z_DIM: 32)
  - Final diversity score: 0.5212
- **FashionMNIST_GAN_hinge_z128** (Loss: hinge, Z_DIM: 128)
  - Final diversity score: 0.4900
- **FashionMNIST_GAN_bce_z64** (Loss: bce, Z_DIM: 64)
  - Final diversity score: 0.5078
- **FashionMNIST_GAN_bce_z32** (Loss: bce, Z_DIM: 32)
  - Final diversity score: 0.5624
- **FashionMNIST_GAN_bce_z128** (Loss: bce, Z_DIM: 128)
  - Final diversity score: 0.5148

## Proxy FID Scores Summary

### GAN FID Scores

- **MNIST_GAN_hinge_z64**: 0.05
- **MNIST_GAN_hinge_z32**: 0.03
- **MNIST_GAN_hinge_z128**: 0.04
- **MNIST_GAN_bce_z64**: 0.05
- **MNIST_GAN_bce_z32**: 0.04
- **MNIST_GAN_bce_z128**: 0.06
- **FashionMNIST_GAN_hinge_z64**: 0.06
- **FashionMNIST_GAN_hinge_z32**: 0.07
- **FashionMNIST_GAN_hinge_z128**: 0.06
- **FashionMNIST_GAN_bce_z64**: 0.08
- **FashionMNIST_GAN_bce_z32**: 0.09
- **FashionMNIST_GAN_bce_z128**: 0.08

### VAE FID Scores

- **MNIST_VAE_latent16**: 0.33
- **MNIST_VAE_latent8**: 0.25
- **MNIST_VAE_latent32**: 0.40
- **FashionMNIST_VAE_latent16**: 0.94
- **FashionMNIST_VAE_latent8**: 0.78
- **FashionMNIST_VAE_latent32**: 0.93

## Reflection Questions & Data-Driven Answers

### 1. What hyperparameters most influenced GAN stability in your runs?

**Analysis Guide:**
- Compare loss curves (D loss and G loss) across different configurations
- Compare FID scores: lower FID = better quality
- Compare diversity scores: higher = more diverse samples
- Look for patterns:
  - Does hinge loss perform better than BCE?
  - Does larger Z_DIM (128) help or hurt?
  - Are there differences between MNIST and FashionMNIST?

**Stability Indicators from Your Experiments:**

**MNIST:**
- Stable configurations (no mode collapse): 6
  - hinge loss, Z_DIM=64
  - hinge loss, Z_DIM=32
  - hinge loss, Z_DIM=128
  - bce loss, Z_DIM=64
  - bce loss, Z_DIM=32
  - bce loss, Z_DIM=128

**FashionMNIST:**
- Stable configurations (no mode collapse): 6
  - hinge loss, Z_DIM=64
  - hinge loss, Z_DIM=32
  - hinge loss, Z_DIM=128
  - bce loss, Z_DIM=64
  - bce loss, Z_DIM=32
  - bce loss, Z_DIM=128

### 2. Evidence of mode collapse (if any)? What helped?

**Answer this question using:**
- The Mode Collapse Summary section above
- Visual inspection of generated samples (check for lack of diversity)
- Diversity scores: lower scores indicate less diversity

**No Mode Collapse Detected:**
- All experiments maintained good diversity
- This suggests your hyperparameters were well-chosen
- You can note: "No mode collapse observed. Stable configurations included [list stable ones]"

### 3. How did latent dim affect VAE reconstructions and samples?

**Analysis Guide:**
- Compare reconstruction losses across latent dimensions (8, 16, 32)
- Compare KL divergence: higher = more regularization
- Visual inspection: look at reconstruction quality and random sample quality
- FID scores: lower = better sample quality

**Latent Dimension Comparison:**

**MNIST:**
- Latent dim 8:
  - Final total loss: 86.7948
  - Final recon loss: 69.3989
  - Final KL loss: 17.3960
  - FID score: 0.25
- Latent dim 16:
  - Final total loss: 78.1758
  - Final recon loss: 52.8648
  - Final KL loss: 25.3110
  - FID score: 0.33
- Latent dim 32:
  - Final total loss: 78.1761
  - Final recon loss: 49.4401
  - Final KL loss: 28.7360
  - FID score: 0.40

**FashionMNIST:**
- Latent dim 8:
  - Final total loss: 110.3554
  - Final recon loss: 93.0578
  - Final KL loss: 17.2976
  - FID score: 0.78
- Latent dim 16:
  - Final total loss: 108.4302
  - Final recon loss: 86.0348
  - Final KL loss: 22.3954
  - FID score: 0.94
- Latent dim 32:
  - Final total loss: 114.6294
  - Final recon loss: 92.4168
  - Final KL loss: 22.2125
  - FID score: 0.93

**Expected patterns:**
- Lower latent dim (8): May have higher reconstruction error, but stronger regularization
- Higher latent dim (32): Better reconstruction, but may have less structured latent space
- Medium (16): Often a good balance

### 4. One idea to combine benefits of both models (e.g., VAE-GAN)

**Consider these approaches:**
- **VAE-GAN**: Use VAE encoder to provide structured latent space, GAN discriminator for sharpness
- **Adversarial VAE**: Add discriminator to VAE to improve sample quality
- **Latent GAN**: Train GAN in VAE's latent space instead of raw noise
- **Hybrid training**: Use VAE for reconstruction, GAN for generation

**Your observations:**
- GAN strengths: Sharp, high-quality samples (when stable)
- VAE strengths: Structured latent space, smooth interpolations, reconstruction capability
- Combination idea: [Write your idea here based on your results]

