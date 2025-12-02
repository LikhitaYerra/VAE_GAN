#!/usr/bin/env python3
"""
Generate plots from experiment results and add them to the report.
"""
import re
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

RESULTS_DIR = "results"
REPORT_PATH = f"{RESULTS_DIR}/experiment_report_20251202_140306.md"

# Parse the report to extract data
def parse_report():
    """Extract data from the markdown report."""
    with open(REPORT_PATH, 'r') as f:
        content = f.read()
    
    gan_data = {}
    vae_data = {}
    
    # Extract GAN data
    gan_sections = re.findall(r'#### (.*?)\n(.*?)(?=####|##)', content, re.DOTALL)
    for exp_name, section in gan_sections:
        if 'GAN' in exp_name:
            data = {}
            if match := re.search(r'Final D Loss: ([\d.]+)', section):
                data['d_loss'] = float(match.group(1))
            if match := re.search(r'Final G Loss: ([\d.]+)', section):
                data['g_loss'] = float(match.group(1))
            if match := re.search(r'Proxy FID Score: ([\d.]+)', section):
                data['fid'] = float(match.group(1))
            if match := re.search(r'Loss Type: (\w+)', section):
                data['loss_type'] = match.group(1)
            if match := re.search(r'Z Dimension: (\d+)', section):
                data['z_dim'] = int(match.group(1))
            if 'MNIST' in exp_name:
                data['dataset'] = 'MNIST'
            elif 'FashionMNIST' in exp_name:
                data['dataset'] = 'FashionMNIST'
            gan_data[exp_name] = data
    
    # Extract VAE data
    vae_sections = re.findall(r'#### (.*?)\n(.*?)(?=####|##)', content, re.DOTALL)
    for exp_name, section in vae_sections:
        if 'VAE' in exp_name:
            data = {}
            if match := re.search(r'Final Total Loss: ([\d.]+)', section):
                data['total_loss'] = float(match.group(1))
            if match := re.search(r'Final Recon Loss: ([\d.]+)', section):
                data['recon_loss'] = float(match.group(1))
            if match := re.search(r'Final KL Loss: ([\d.]+)', section):
                data['kl_loss'] = float(match.group(1))
            if match := re.search(r'Proxy FID Score: ([\d.]+)', section):
                data['fid'] = float(match.group(1))
            if match := re.search(r'Latent Dimension: (\d+)', section):
                data['latent_dim'] = int(match.group(1))
            if 'MNIST' in exp_name:
                data['dataset'] = 'MNIST'
            elif 'FashionMNIST' in exp_name:
                data['dataset'] = 'FashionMNIST'
            vae_data[exp_name] = data
    
    return gan_data, vae_data

# Generate plots
def create_plots(gan_data, vae_data):
    """Create various plots from the data."""
    os.makedirs(f"{RESULTS_DIR}/plots", exist_ok=True)
    
    # 1. GAN FID Scores Comparison
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # MNIST GAN FID
    mnist_gan = {k: v for k, v in gan_data.items() if v.get('dataset') == 'MNIST'}
    mnist_labels = [k.replace('MNIST_GAN_', '').replace('_', ' ') for k in mnist_gan.keys()]
    mnist_fids = [v.get('fid', 0) for v in mnist_gan.values()]
    ax1.bar(range(len(mnist_labels)), mnist_fids, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'])
    ax1.set_xticks(range(len(mnist_labels)))
    ax1.set_xticklabels(mnist_labels, rotation=45, ha='right')
    ax1.set_ylabel('FID Score')
    ax1.set_title('GAN FID Scores - MNIST')
    ax1.grid(axis='y', alpha=0.3)
    
    # FashionMNIST GAN FID
    fashion_gan = {k: v for k, v in gan_data.items() if v.get('dataset') == 'FashionMNIST'}
    fashion_labels = [k.replace('FashionMNIST_GAN_', '').replace('_', ' ') for k in fashion_gan.keys()]
    fashion_fids = [v.get('fid', 0) for v in fashion_gan.values()]
    ax2.bar(range(len(fashion_labels)), fashion_fids, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'])
    ax2.set_xticks(range(len(fashion_labels)))
    ax2.set_xticklabels(fashion_labels, rotation=45, ha='right')
    ax2.set_ylabel('FID Score')
    ax2.set_title('GAN FID Scores - FashionMNIST')
    ax2.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f"{RESULTS_DIR}/plots/gan_fid_comparison.png", dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {RESULTS_DIR}/plots/gan_fid_comparison.png")
    
    # 2. VAE FID Scores Comparison
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # MNIST VAE FID
    mnist_vae = {k: v for k, v in vae_data.items() if v.get('dataset') == 'MNIST'}
    mnist_vae_labels = [f"Latent {v.get('latent_dim', '?')}" for v in mnist_vae.values()]
    mnist_vae_fids = [v.get('fid', 0) for v in mnist_vae.values()]
    ax1.bar(mnist_vae_labels, mnist_vae_fids, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
    ax1.set_ylabel('FID Score')
    ax1.set_title('VAE FID Scores - MNIST')
    ax1.grid(axis='y', alpha=0.3)
    
    # FashionMNIST VAE FID
    fashion_vae = {k: v for k, v in vae_data.items() if v.get('dataset') == 'FashionMNIST'}
    fashion_vae_labels = [f"Latent {v.get('latent_dim', '?')}" for v in fashion_vae.values()]
    fashion_vae_fids = [v.get('fid', 0) for v in fashion_vae.values()]
    ax2.bar(fashion_vae_labels, fashion_vae_fids, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
    ax2.set_ylabel('FID Score')
    ax2.set_title('VAE FID Scores - FashionMNIST')
    ax2.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f"{RESULTS_DIR}/plots/vae_fid_comparison.png", dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {RESULTS_DIR}/plots/vae_fid_comparison.png")
    
    # 3. GAN Loss Comparison (D vs G)
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # MNIST - Hinge
    mnist_hinge = {k: v for k, v in mnist_gan.items() if v.get('loss_type') == 'hinge'}
    mnist_hinge_z = [v.get('z_dim', 0) for v in mnist_hinge.values()]
    mnist_hinge_d = [v.get('d_loss', 0) for v in mnist_hinge.values()]
    mnist_hinge_g = [v.get('g_loss', 0) for v in mnist_hinge.values()]
    x = np.arange(len(mnist_hinge_z))
    width = 0.35
    axes[0, 0].bar(x - width/2, mnist_hinge_d, width, label='D Loss', alpha=0.8)
    axes[0, 0].bar(x + width/2, mnist_hinge_g, width, label='G Loss', alpha=0.8)
    axes[0, 0].set_xticks(x)
    axes[0, 0].set_xticklabels([f"Z={z}" for z in mnist_hinge_z])
    axes[0, 0].set_ylabel('Loss')
    axes[0, 0].set_title('MNIST - Hinge Loss')
    axes[0, 0].legend()
    axes[0, 0].grid(axis='y', alpha=0.3)
    
    # MNIST - BCE
    mnist_bce = {k: v for k, v in mnist_gan.items() if v.get('loss_type') == 'bce'}
    mnist_bce_z = [v.get('z_dim', 0) for v in mnist_bce.values()]
    mnist_bce_d = [v.get('d_loss', 0) for v in mnist_bce.values()]
    mnist_bce_g = [v.get('g_loss', 0) for v in mnist_bce.values()]
    x = np.arange(len(mnist_bce_z))
    axes[0, 1].bar(x - width/2, mnist_bce_d, width, label='D Loss', alpha=0.8)
    axes[0, 1].bar(x + width/2, mnist_bce_g, width, label='G Loss', alpha=0.8)
    axes[0, 1].set_xticks(x)
    axes[0, 1].set_xticklabels([f"Z={z}" for z in mnist_bce_z])
    axes[0, 1].set_ylabel('Loss')
    axes[0, 1].set_title('MNIST - BCE Loss')
    axes[0, 1].legend()
    axes[0, 1].grid(axis='y', alpha=0.3)
    
    # FashionMNIST - Hinge
    fashion_hinge = {k: v for k, v in fashion_gan.items() if v.get('loss_type') == 'hinge'}
    fashion_hinge_z = [v.get('z_dim', 0) for v in fashion_hinge.values()]
    fashion_hinge_d = [v.get('d_loss', 0) for v in fashion_hinge.values()]
    fashion_hinge_g = [v.get('g_loss', 0) for v in fashion_hinge.values()]
    x = np.arange(len(fashion_hinge_z))
    axes[1, 0].bar(x - width/2, fashion_hinge_d, width, label='D Loss', alpha=0.8)
    axes[1, 0].bar(x + width/2, fashion_hinge_g, width, label='G Loss', alpha=0.8)
    axes[1, 0].set_xticks(x)
    axes[1, 0].set_xticklabels([f"Z={z}" for z in fashion_hinge_z])
    axes[1, 0].set_ylabel('Loss')
    axes[1, 0].set_title('FashionMNIST - Hinge Loss')
    axes[1, 0].legend()
    axes[1, 0].grid(axis='y', alpha=0.3)
    
    # FashionMNIST - BCE
    fashion_bce = {k: v for k, v in fashion_gan.items() if v.get('loss_type') == 'bce'}
    fashion_bce_z = [v.get('z_dim', 0) for v in fashion_bce.values()]
    fashion_bce_d = [v.get('d_loss', 0) for v in fashion_bce.values()]
    fashion_bce_g = [v.get('g_loss', 0) for v in fashion_bce.values()]
    x = np.arange(len(fashion_bce_z))
    axes[1, 1].bar(x - width/2, fashion_bce_d, width, label='D Loss', alpha=0.8)
    axes[1, 1].bar(x + width/2, fashion_bce_g, width, label='G Loss', alpha=0.8)
    axes[1, 1].set_xticks(x)
    axes[1, 1].set_xticklabels([f"Z={z}" for z in fashion_bce_z])
    axes[1, 1].set_ylabel('Loss')
    axes[1, 1].set_title('FashionMNIST - BCE Loss')
    axes[1, 1].legend()
    axes[1, 1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f"{RESULTS_DIR}/plots/gan_loss_comparison.png", dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {RESULTS_DIR}/plots/gan_loss_comparison.png")
    
    # 4. VAE Loss Comparison
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # MNIST - Total Loss
    mnist_vae_sorted = sorted(mnist_vae.items(), key=lambda x: x[1].get('latent_dim', 0))
    mnist_latents = [v.get('latent_dim', 0) for _, v in mnist_vae_sorted]
    mnist_total = [v.get('total_loss', 0) for _, v in mnist_vae_sorted]
    mnist_recon = [v.get('recon_loss', 0) for _, v in mnist_vae_sorted]
    mnist_kl = [v.get('kl_loss', 0) for _, v in mnist_vae_sorted]
    x = np.arange(len(mnist_latents))
    width = 0.25
    axes[0, 0].bar(x - width, mnist_total, width, label='Total', alpha=0.8)
    axes[0, 0].bar(x, mnist_recon, width, label='Recon', alpha=0.8)
    axes[0, 0].bar(x + width, mnist_kl, width, label='KL', alpha=0.8)
    axes[0, 0].set_xticks(x)
    axes[0, 0].set_xticklabels([f"Latent {z}" for z in mnist_latents])
    axes[0, 0].set_ylabel('Loss')
    axes[0, 0].set_title('MNIST - VAE Losses')
    axes[0, 0].legend()
    axes[0, 0].grid(axis='y', alpha=0.3)
    
    # FashionMNIST - Total Loss
    fashion_vae_sorted = sorted(fashion_vae.items(), key=lambda x: x[1].get('latent_dim', 0))
    fashion_latents = [v.get('latent_dim', 0) for _, v in fashion_vae_sorted]
    fashion_total = [v.get('total_loss', 0) for _, v in fashion_vae_sorted]
    fashion_recon = [v.get('recon_loss', 0) for _, v in fashion_vae_sorted]
    fashion_kl = [v.get('kl_loss', 0) for _, v in fashion_vae_sorted]
    x = np.arange(len(fashion_latents))
    axes[0, 1].bar(x - width, fashion_total, width, label='Total', alpha=0.8)
    axes[0, 1].bar(x, fashion_recon, width, label='Recon', alpha=0.8)
    axes[0, 1].bar(x + width, fashion_kl, width, label='KL', alpha=0.8)
    axes[0, 1].set_xticks(x)
    axes[0, 1].set_xticklabels([f"Latent {z}" for z in fashion_latents])
    axes[0, 1].set_ylabel('Loss')
    axes[0, 1].set_title('FashionMNIST - VAE Losses')
    axes[0, 1].legend()
    axes[0, 1].grid(axis='y', alpha=0.3)
    
    # MNIST - FID by Latent Dim
    axes[1, 0].bar(mnist_vae_labels, mnist_vae_fids, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
    axes[1, 0].set_ylabel('FID Score')
    axes[1, 0].set_title('MNIST - VAE FID by Latent Dim')
    axes[1, 0].grid(axis='y', alpha=0.3)
    
    # FashionMNIST - FID by Latent Dim
    axes[1, 1].bar(fashion_vae_labels, fashion_vae_fids, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
    axes[1, 1].set_ylabel('FID Score')
    axes[1, 1].set_title('FashionMNIST - VAE FID by Latent Dim')
    axes[1, 1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f"{RESULTS_DIR}/plots/vae_loss_comparison.png", dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {RESULTS_DIR}/plots/vae_loss_comparison.png")
    
    # 5. Overall FID Comparison (GAN vs VAE)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # MNIST
    gan_mnist_avg = np.mean(mnist_fids)
    vae_mnist_avg = np.mean(mnist_vae_fids)
    ax1.bar(['GAN (avg)', 'VAE (avg)'], [gan_mnist_avg, vae_mnist_avg], 
            color=['#2ca02c', '#d62728'], alpha=0.7)
    ax1.set_ylabel('Average FID Score')
    ax1.set_title('MNIST - Average FID: GAN vs VAE')
    ax1.grid(axis='y', alpha=0.3)
    ax1.text(0, gan_mnist_avg + 0.01, f'{gan_mnist_avg:.3f}', ha='center', va='bottom')
    ax1.text(1, vae_mnist_avg + 0.01, f'{vae_mnist_avg:.3f}', ha='center', va='bottom')
    
    # FashionMNIST
    gan_fashion_avg = np.mean(fashion_fids)
    vae_fashion_avg = np.mean(fashion_vae_fids)
    ax2.bar(['GAN (avg)', 'VAE (avg)'], [gan_fashion_avg, vae_fashion_avg], 
            color=['#2ca02c', '#d62728'], alpha=0.7)
    ax2.set_ylabel('Average FID Score')
    ax2.set_title('FashionMNIST - Average FID: GAN vs VAE')
    ax2.grid(axis='y', alpha=0.3)
    ax2.text(0, gan_fashion_avg + 0.01, f'{gan_fashion_avg:.3f}', ha='center', va='bottom')
    ax2.text(1, vae_fashion_avg + 0.01, f'{vae_fashion_avg:.3f}', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig(f"{RESULTS_DIR}/plots/fid_gan_vs_vae.png", dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {RESULTS_DIR}/plots/fid_gan_vs_vae.png")

if __name__ == "__main__":
    import os
    gan_data, vae_data = parse_report()
    create_plots(gan_data, vae_data)
    print("\nAll plots generated successfully!")

