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
    
    # Extract GAN data - improved regex
    gan_sections = re.findall(r'#### (.*?)\n(.*?)(?=####|##)', content, re.DOTALL)
    for exp_name, section in gan_sections:
        if 'GAN' in exp_name:
            data = {}
            if match := re.search(r'\*\*Final D Loss:\*\* ([\d.]+)', section):
                data['d_loss'] = float(match.group(1))
            elif match := re.search(r'Final D Loss: ([\d.]+)', section):
                data['d_loss'] = float(match.group(1))
            if match := re.search(r'\*\*Final G Loss:\*\* ([\d.]+)', section):
                data['g_loss'] = float(match.group(1))
            elif match := re.search(r'Final G Loss: ([\d.]+)', section):
                data['g_loss'] = float(match.group(1))
            if match := re.search(r'\*\*Proxy FID Score:\*\* ([\d.]+)', section):
                data['fid'] = float(match.group(1))
            elif match := re.search(r'Proxy FID Score: ([\d.]+)', section):
                data['fid'] = float(match.group(1))
            if match := re.search(r'\*\*Loss Type:\*\* (\w+)', section):
                data['loss_type'] = match.group(1)
            elif match := re.search(r'Loss Type: (\w+)', section):
                data['loss_type'] = match.group(1)
            if match := re.search(r'\*\*Z Dimension:\*\* (\d+)', section):
                data['z_dim'] = int(match.group(1))
            elif match := re.search(r'Z Dimension: (\d+)', section):
                data['z_dim'] = int(match.group(1))
            if 'MNIST' in exp_name and 'FashionMNIST' not in exp_name:
                data['dataset'] = 'MNIST'
            elif 'FashionMNIST' in exp_name:
                data['dataset'] = 'FashionMNIST'
            if data:  # Only add if we found some data
                gan_data[exp_name] = data
    
    # Extract VAE data - improved regex
    vae_sections = re.findall(r'#### (.*?)\n(.*?)(?=####|##)', content, re.DOTALL)
    for exp_name, section in vae_sections:
        if 'VAE' in exp_name:
            data = {}
            if match := re.search(r'\*\*Final Total Loss:\*\* ([\d.]+)', section):
                data['total_loss'] = float(match.group(1))
            elif match := re.search(r'Final Total Loss: ([\d.]+)', section):
                data['total_loss'] = float(match.group(1))
            if match := re.search(r'\*\*Final Recon Loss:\*\* ([\d.]+)', section):
                data['recon_loss'] = float(match.group(1))
            elif match := re.search(r'Final Recon Loss: ([\d.]+)', section):
                data['recon_loss'] = float(match.group(1))
            if match := re.search(r'\*\*Final KL Loss:\*\* ([\d.]+)', section):
                data['kl_loss'] = float(match.group(1))
            elif match := re.search(r'Final KL Loss: ([\d.]+)', section):
                data['kl_loss'] = float(match.group(1))
            if match := re.search(r'\*\*Proxy FID Score:\*\* ([\d.]+)', section):
                data['fid'] = float(match.group(1))
            elif match := re.search(r'Proxy FID Score: ([\d.]+)', section):
                data['fid'] = float(match.group(1))
            if match := re.search(r'\*\*Latent Dimension:\*\* (\d+)', section):
                data['latent_dim'] = int(match.group(1))
            elif match := re.search(r'Latent Dimension: (\d+)', section):
                data['latent_dim'] = int(match.group(1))
            if 'MNIST' in exp_name and 'FashionMNIST' not in exp_name:
                data['dataset'] = 'MNIST'
            elif 'FashionMNIST' in exp_name:
                data['dataset'] = 'FashionMNIST'
            if data:  # Only add if we found some data
                vae_data[exp_name] = data
    
    return gan_data, vae_data

# Generate plots
def create_plots(gan_data, vae_data):
    """Create various plots from the data."""
    import os
    os.makedirs(f"{RESULTS_DIR}/plots", exist_ok=True)
    
    # Debug: print what we extracted
    print(f"\nExtracted {len(gan_data)} GAN experiments")
    print(f"Extracted {len(vae_data)} VAE experiments")
    if gan_data:
        print(f"Sample GAN data: {list(gan_data.items())[0]}")
    if vae_data:
        print(f"Sample VAE data: {list(vae_data.items())[0]}")
    
    # 1. GAN FID Scores Comparison
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # MNIST GAN FID
    mnist_gan = {k: v for k, v in gan_data.items() if v.get('dataset') == 'MNIST'}
    if not mnist_gan:
        print("Warning: No MNIST GAN data found")
        return
    
    # Sort by loss_type and z_dim for consistent ordering
    mnist_gan_sorted = sorted(mnist_gan.items(), key=lambda x: (x[1].get('loss_type', ''), x[1].get('z_dim', 0)))
    mnist_labels = [f"{v.get('loss_type', '?')} z{v.get('z_dim', '?')}" for _, v in mnist_gan_sorted]
    mnist_fids = [v.get('fid', 0) for _, v in mnist_gan_sorted]
    
    if len(mnist_fids) > 0 and max(mnist_fids) > 0:
        bars = ax1.bar(range(len(mnist_labels)), mnist_fids, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'][:len(mnist_labels)])
        ax1.set_xticks(range(len(mnist_labels)))
        ax1.set_xticklabels(mnist_labels, rotation=45, ha='right')
        ax1.set_ylabel('FID Score', fontsize=11)
        ax1.set_title('GAN FID Scores - MNIST', fontsize=12, fontweight='bold')
        ax1.grid(axis='y', alpha=0.3)
        ax1.set_ylim(0, max(mnist_fids) * 1.3 if max(mnist_fids) > 0 else 0.1)
        # Add value labels on bars
        for i, (bar, v) in enumerate(zip(bars, mnist_fids)):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + max(mnist_fids) * 0.02,
                    f'{v:.2f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
    else:
        ax1.text(0.5, 0.5, 'No data available', ha='center', va='center', transform=ax1.transAxes)
        ax1.set_title('GAN FID Scores - MNIST (No Data)')
    
    # FashionMNIST GAN FID
    fashion_gan = {k: v for k, v in gan_data.items() if v.get('dataset') == 'FashionMNIST'}
    if not fashion_gan:
        print("Warning: No FashionMNIST GAN data found")
        ax2.text(0.5, 0.5, 'No data available', ha='center', va='center', transform=ax2.transAxes)
        ax2.set_title('GAN FID Scores - FashionMNIST (No Data)')
    else:
        # Sort by loss_type and z_dim for consistent ordering
        fashion_gan_sorted = sorted(fashion_gan.items(), key=lambda x: (x[1].get('loss_type', ''), x[1].get('z_dim', 0)))
        fashion_labels = [f"{v.get('loss_type', '?')} z{v.get('z_dim', '?')}" for _, v in fashion_gan_sorted]
        fashion_fids = [v.get('fid', 0) for _, v in fashion_gan_sorted]
        
        if len(fashion_fids) > 0 and max(fashion_fids) > 0:
            bars = ax2.bar(range(len(fashion_labels)), fashion_fids, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'][:len(fashion_labels)])
            ax2.set_xticks(range(len(fashion_labels)))
            ax2.set_xticklabels(fashion_labels, rotation=45, ha='right')
            ax2.set_ylabel('FID Score', fontsize=11)
            ax2.set_title('GAN FID Scores - FashionMNIST', fontsize=12, fontweight='bold')
            ax2.grid(axis='y', alpha=0.3)
            ax2.set_ylim(0, max(fashion_fids) * 1.3 if max(fashion_fids) > 0 else 0.1)
            # Add value labels on bars
            for i, (bar, v) in enumerate(zip(bars, fashion_fids)):
                height = bar.get_height()
                ax2.text(bar.get_x() + bar.get_width()/2., height + max(fashion_fids) * 0.02,
                        f'{v:.2f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
        else:
            ax2.text(0.5, 0.5, 'No data available', ha='center', va='center', transform=ax2.transAxes)
            ax2.set_title('GAN FID Scores - FashionMNIST (No Data)')
    
    plt.tight_layout()
    plt.savefig(f"{RESULTS_DIR}/plots/gan_fid_comparison.png", dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {RESULTS_DIR}/plots/gan_fid_comparison.png")
    
    # 2. VAE FID Scores Comparison
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # MNIST VAE FID
    mnist_vae = {k: v for k, v in vae_data.items() if v.get('dataset') == 'MNIST'}
    if mnist_vae:
        mnist_vae_sorted = sorted(mnist_vae.items(), key=lambda x: x[1].get('latent_dim', 0))
        mnist_vae_labels = [f"Latent {v.get('latent_dim', '?')}" for _, v in mnist_vae_sorted]
        mnist_vae_fids = [v.get('fid', 0) for _, v in mnist_vae_sorted]
        if len(mnist_vae_fids) > 0:
            ax1.bar(mnist_vae_labels, mnist_vae_fids, color=['#1f77b4', '#ff7f0e', '#2ca02c'][:len(mnist_vae_labels)])
            ax1.set_ylabel('FID Score')
            ax1.set_title('VAE FID Scores - MNIST')
            ax1.grid(axis='y', alpha=0.3)
            # Add value labels
            for i, v in enumerate(mnist_vae_fids):
                ax1.text(i, v + 0.01, f'{v:.2f}', ha='center', va='bottom', fontsize=8)
        else:
            ax1.text(0.5, 0.5, 'No data available', ha='center', va='center', transform=ax1.transAxes)
            ax1.set_title('VAE FID Scores - MNIST (No Data)')
    else:
        ax1.text(0.5, 0.5, 'No data available', ha='center', va='center', transform=ax1.transAxes)
        ax1.set_title('VAE FID Scores - MNIST (No Data)')
        mnist_vae_fids = []
    
    # FashionMNIST VAE FID
    fashion_vae = {k: v for k, v in vae_data.items() if v.get('dataset') == 'FashionMNIST'}
    if fashion_vae:
        fashion_vae_sorted = sorted(fashion_vae.items(), key=lambda x: x[1].get('latent_dim', 0))
        fashion_vae_labels = [f"Latent {v.get('latent_dim', '?')}" for _, v in fashion_vae_sorted]
        fashion_vae_fids = [v.get('fid', 0) for _, v in fashion_vae_sorted]
        if len(fashion_vae_fids) > 0:
            ax2.bar(fashion_vae_labels, fashion_vae_fids, color=['#1f77b4', '#ff7f0e', '#2ca02c'][:len(fashion_vae_labels)])
            ax2.set_ylabel('FID Score')
            ax2.set_title('VAE FID Scores - FashionMNIST')
            ax2.grid(axis='y', alpha=0.3)
            # Add value labels
            for i, v in enumerate(fashion_vae_fids):
                ax2.text(i, v + 0.01, f'{v:.2f}', ha='center', va='bottom', fontsize=8)
        else:
            ax2.text(0.5, 0.5, 'No data available', ha='center', va='center', transform=ax2.transAxes)
            ax2.set_title('VAE FID Scores - FashionMNIST (No Data)')
    else:
        ax2.text(0.5, 0.5, 'No data available', ha='center', va='center', transform=ax2.transAxes)
        ax2.set_title('VAE FID Scores - FashionMNIST (No Data)')
        fashion_vae_fids = []
    
    plt.tight_layout()
    plt.savefig(f"{RESULTS_DIR}/plots/vae_fid_comparison.png", dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {RESULTS_DIR}/plots/vae_fid_comparison.png")
    
    # 3. GAN Loss Comparison (D vs G)
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # MNIST - Hinge
    mnist_hinge = {k: v for k, v in mnist_gan.items() if v.get('loss_type') == 'hinge'}
    if mnist_hinge:
        mnist_hinge_sorted = sorted(mnist_hinge.items(), key=lambda x: x[1].get('z_dim', 0))
        mnist_hinge_z = [v.get('z_dim', 0) for _, v in mnist_hinge_sorted]
        mnist_hinge_d = [v.get('d_loss', 0) for _, v in mnist_hinge_sorted]
        mnist_hinge_g = [v.get('g_loss', 0) for _, v in mnist_hinge_sorted]
        if len(mnist_hinge_z) > 0:
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
        else:
            axes[0, 0].text(0.5, 0.5, 'No data available', ha='center', va='center', transform=axes[0, 0].transAxes)
            axes[0, 0].set_title('MNIST - Hinge Loss (No Data)')
    else:
        axes[0, 0].text(0.5, 0.5, 'No data available', ha='center', va='center', transform=axes[0, 0].transAxes)
        axes[0, 0].set_title('MNIST - Hinge Loss (No Data)')
    
    # MNIST - BCE
    mnist_bce = {k: v for k, v in mnist_gan.items() if v.get('loss_type') == 'bce'}
    if mnist_bce:
        mnist_bce_sorted = sorted(mnist_bce.items(), key=lambda x: x[1].get('z_dim', 0))
        mnist_bce_z = [v.get('z_dim', 0) for _, v in mnist_bce_sorted]
        mnist_bce_d = [v.get('d_loss', 0) for _, v in mnist_bce_sorted]
        mnist_bce_g = [v.get('g_loss', 0) for _, v in mnist_bce_sorted]
        if len(mnist_bce_z) > 0:
            x = np.arange(len(mnist_bce_z))
            axes[0, 1].bar(x - width/2, mnist_bce_d, width, label='D Loss', alpha=0.8)
            axes[0, 1].bar(x + width/2, mnist_bce_g, width, label='G Loss', alpha=0.8)
            axes[0, 1].set_xticks(x)
            axes[0, 1].set_xticklabels([f"Z={z}" for z in mnist_bce_z])
            axes[0, 1].set_ylabel('Loss')
            axes[0, 1].set_title('MNIST - BCE Loss')
            axes[0, 1].legend()
            axes[0, 1].grid(axis='y', alpha=0.3)
        else:
            axes[0, 1].text(0.5, 0.5, 'No data available', ha='center', va='center', transform=axes[0, 1].transAxes)
            axes[0, 1].set_title('MNIST - BCE Loss (No Data)')
    else:
        axes[0, 1].text(0.5, 0.5, 'No data available', ha='center', va='center', transform=axes[0, 1].transAxes)
        axes[0, 1].set_title('MNIST - BCE Loss (No Data)')
    
    # FashionMNIST - Hinge
    fashion_hinge = {k: v for k, v in fashion_gan.items() if v.get('loss_type') == 'hinge'}
    if fashion_hinge:
        fashion_hinge_sorted = sorted(fashion_hinge.items(), key=lambda x: x[1].get('z_dim', 0))
        fashion_hinge_z = [v.get('z_dim', 0) for _, v in fashion_hinge_sorted]
        fashion_hinge_d = [v.get('d_loss', 0) for _, v in fashion_hinge_sorted]
        fashion_hinge_g = [v.get('g_loss', 0) for _, v in fashion_hinge_sorted]
        if len(fashion_hinge_z) > 0:
            x = np.arange(len(fashion_hinge_z))
            axes[1, 0].bar(x - width/2, fashion_hinge_d, width, label='D Loss', alpha=0.8)
            axes[1, 0].bar(x + width/2, fashion_hinge_g, width, label='G Loss', alpha=0.8)
            axes[1, 0].set_xticks(x)
            axes[1, 0].set_xticklabels([f"Z={z}" for z in fashion_hinge_z])
            axes[1, 0].set_ylabel('Loss')
            axes[1, 0].set_title('FashionMNIST - Hinge Loss')
            axes[1, 0].legend()
            axes[1, 0].grid(axis='y', alpha=0.3)
        else:
            axes[1, 0].text(0.5, 0.5, 'No data available', ha='center', va='center', transform=axes[1, 0].transAxes)
            axes[1, 0].set_title('FashionMNIST - Hinge Loss (No Data)')
    else:
        axes[1, 0].text(0.5, 0.5, 'No data available', ha='center', va='center', transform=axes[1, 0].transAxes)
        axes[1, 0].set_title('FashionMNIST - Hinge Loss (No Data)')
    
    # FashionMNIST - BCE
    fashion_bce = {k: v for k, v in fashion_gan.items() if v.get('loss_type') == 'bce'}
    if fashion_bce:
        fashion_bce_sorted = sorted(fashion_bce.items(), key=lambda x: x[1].get('z_dim', 0))
        fashion_bce_z = [v.get('z_dim', 0) for _, v in fashion_bce_sorted]
        fashion_bce_d = [v.get('d_loss', 0) for _, v in fashion_bce_sorted]
        fashion_bce_g = [v.get('g_loss', 0) for _, v in fashion_bce_sorted]
        if len(fashion_bce_z) > 0:
            x = np.arange(len(fashion_bce_z))
            axes[1, 1].bar(x - width/2, fashion_bce_d, width, label='D Loss', alpha=0.8)
            axes[1, 1].bar(x + width/2, fashion_bce_g, width, label='G Loss', alpha=0.8)
            axes[1, 1].set_xticks(x)
            axes[1, 1].set_xticklabels([f"Z={z}" for z in fashion_bce_z])
            axes[1, 1].set_ylabel('Loss')
            axes[1, 1].set_title('FashionMNIST - BCE Loss')
            axes[1, 1].legend()
            axes[1, 1].grid(axis='y', alpha=0.3)
        else:
            axes[1, 1].text(0.5, 0.5, 'No data available', ha='center', va='center', transform=axes[1, 1].transAxes)
            axes[1, 1].set_title('FashionMNIST - BCE Loss (No Data)')
    else:
        axes[1, 1].text(0.5, 0.5, 'No data available', ha='center', va='center', transform=axes[1, 1].transAxes)
        axes[1, 1].set_title('FashionMNIST - BCE Loss (No Data)')
    
    plt.tight_layout()
    plt.savefig(f"{RESULTS_DIR}/plots/gan_loss_comparison.png", dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {RESULTS_DIR}/plots/gan_loss_comparison.png")
    
    # 4. VAE Loss Comparison
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Re-extract VAE data for this section
    mnist_vae = {k: v for k, v in vae_data.items() if v.get('dataset') == 'MNIST'}
    fashion_vae = {k: v for k, v in vae_data.items() if v.get('dataset') == 'FashionMNIST'}
    
    # MNIST - Total Loss
    if mnist_vae:
        mnist_vae_sorted = sorted(mnist_vae.items(), key=lambda x: x[1].get('latent_dim', 0))
        mnist_latents = [v.get('latent_dim', 0) for _, v in mnist_vae_sorted]
        mnist_total = [v.get('total_loss', 0) for _, v in mnist_vae_sorted]
        mnist_recon = [v.get('recon_loss', 0) for _, v in mnist_vae_sorted]
        mnist_kl = [v.get('kl_loss', 0) for _, v in mnist_vae_sorted]
        if len(mnist_latents) > 0:
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
        else:
            axes[0, 0].text(0.5, 0.5, 'No data available', ha='center', va='center', transform=axes[0, 0].transAxes)
            axes[0, 0].set_title('MNIST - VAE Losses (No Data)')
    else:
        axes[0, 0].text(0.5, 0.5, 'No data available', ha='center', va='center', transform=axes[0, 0].transAxes)
        axes[0, 0].set_title('MNIST - VAE Losses (No Data)')
    
    # FashionMNIST - Total Loss
    if fashion_vae:
        fashion_vae_sorted = sorted(fashion_vae.items(), key=lambda x: x[1].get('latent_dim', 0))
        fashion_latents = [v.get('latent_dim', 0) for _, v in fashion_vae_sorted]
        fashion_total = [v.get('total_loss', 0) for _, v in fashion_vae_sorted]
        fashion_recon = [v.get('recon_loss', 0) for _, v in fashion_vae_sorted]
        fashion_kl = [v.get('kl_loss', 0) for _, v in fashion_vae_sorted]
        if len(fashion_latents) > 0:
            x = np.arange(len(fashion_latents))
            width = 0.25
            axes[0, 1].bar(x - width, fashion_total, width, label='Total', alpha=0.8)
            axes[0, 1].bar(x, fashion_recon, width, label='Recon', alpha=0.8)
            axes[0, 1].bar(x + width, fashion_kl, width, label='KL', alpha=0.8)
            axes[0, 1].set_xticks(x)
            axes[0, 1].set_xticklabels([f"Latent {z}" for z in fashion_latents])
            axes[0, 1].set_ylabel('Loss')
            axes[0, 1].set_title('FashionMNIST - VAE Losses')
            axes[0, 1].legend()
            axes[0, 1].grid(axis='y', alpha=0.3)
        else:
            axes[0, 1].text(0.5, 0.5, 'No data available', ha='center', va='center', transform=axes[0, 1].transAxes)
            axes[0, 1].set_title('FashionMNIST - VAE Losses (No Data)')
    else:
        axes[0, 1].text(0.5, 0.5, 'No data available', ha='center', va='center', transform=axes[0, 1].transAxes)
        axes[0, 1].set_title('FashionMNIST - VAE Losses (No Data)')
    
    # MNIST - FID by Latent Dim (reuse sorted data)
    if mnist_vae and 'mnist_vae_sorted' in locals():
        mnist_vae_labels = [f"Latent {v.get('latent_dim', '?')}" for _, v in mnist_vae_sorted]
        mnist_vae_fids = [v.get('fid', 0) for _, v in mnist_vae_sorted]
        if len(mnist_vae_fids) > 0:
            axes[1, 0].bar(mnist_vae_labels, mnist_vae_fids, color=['#1f77b4', '#ff7f0e', '#2ca02c'][:len(mnist_vae_labels)])
            axes[1, 0].set_ylabel('FID Score')
            axes[1, 0].set_title('MNIST - VAE FID by Latent Dim')
            axes[1, 0].grid(axis='y', alpha=0.3)
        else:
            axes[1, 0].text(0.5, 0.5, 'No data available', ha='center', va='center', transform=axes[1, 0].transAxes)
            axes[1, 0].set_title('MNIST - VAE FID by Latent Dim (No Data)')
    else:
        axes[1, 0].text(0.5, 0.5, 'No data available', ha='center', va='center', transform=axes[1, 0].transAxes)
        axes[1, 0].set_title('MNIST - VAE FID by Latent Dim (No Data)')
    
    # FashionMNIST - FID by Latent Dim (reuse sorted data)
    if fashion_vae and 'fashion_vae_sorted' in locals():
        fashion_vae_labels = [f"Latent {v.get('latent_dim', '?')}" for _, v in fashion_vae_sorted]
        fashion_vae_fids = [v.get('fid', 0) for _, v in fashion_vae_sorted]
        if len(fashion_vae_fids) > 0:
            axes[1, 1].bar(fashion_vae_labels, fashion_vae_fids, color=['#1f77b4', '#ff7f0e', '#2ca02c'][:len(fashion_vae_labels)])
            axes[1, 1].set_ylabel('FID Score')
            axes[1, 1].set_title('FashionMNIST - VAE FID by Latent Dim')
            axes[1, 1].grid(axis='y', alpha=0.3)
        else:
            axes[1, 1].text(0.5, 0.5, 'No data available', ha='center', va='center', transform=axes[1, 1].transAxes)
            axes[1, 1].set_title('FashionMNIST - VAE FID by Latent Dim (No Data)')
    else:
        axes[1, 1].text(0.5, 0.5, 'No data available', ha='center', va='center', transform=axes[1, 1].transAxes)
        axes[1, 1].set_title('FashionMNIST - VAE FID by Latent Dim (No Data)')
    
    plt.tight_layout()
    plt.savefig(f"{RESULTS_DIR}/plots/vae_loss_comparison.png", dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {RESULTS_DIR}/plots/vae_loss_comparison.png")
    
    # 5. Overall FID Comparison (GAN vs VAE)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Re-extract data for this plot
    mnist_gan = {k: v for k, v in gan_data.items() if v.get('dataset') == 'MNIST'}
    fashion_gan = {k: v for k, v in gan_data.items() if v.get('dataset') == 'FashionMNIST'}
    mnist_vae = {k: v for k, v in vae_data.items() if v.get('dataset') == 'MNIST'}
    fashion_vae = {k: v for k, v in vae_data.items() if v.get('dataset') == 'FashionMNIST'}
    
    # MNIST
    mnist_gan_fids = [v.get('fid', 0) for v in mnist_gan.values() if v.get('fid', 0) > 0]
    mnist_vae_fids_list = [v.get('fid', 0) for v in mnist_vae.values() if v.get('fid', 0) > 0]
    
    if mnist_gan_fids and mnist_vae_fids_list:
        gan_mnist_avg = np.mean(mnist_gan_fids)
        vae_mnist_avg = np.mean(mnist_vae_fids_list)
        ax1.bar(['GAN (avg)', 'VAE (avg)'], [gan_mnist_avg, vae_mnist_avg], 
                color=['#2ca02c', '#d62728'], alpha=0.7)
        ax1.set_ylabel('Average FID Score')
        ax1.set_title('MNIST - Average FID: GAN vs VAE')
        ax1.grid(axis='y', alpha=0.3)
        ax1.text(0, gan_mnist_avg + 0.01, f'{gan_mnist_avg:.3f}', ha='center', va='bottom')
        ax1.text(1, vae_mnist_avg + 0.01, f'{vae_mnist_avg:.3f}', ha='center', va='bottom')
    else:
        ax1.text(0.5, 0.5, 'No data available', ha='center', va='center', transform=ax1.transAxes)
        ax1.set_title('MNIST - Average FID: GAN vs VAE (No Data)')
    
    # FashionMNIST
    fashion_gan_fids = [v.get('fid', 0) for v in fashion_gan.values() if v.get('fid', 0) > 0]
    fashion_vae_fids_list = [v.get('fid', 0) for v in fashion_vae.values() if v.get('fid', 0) > 0]
    
    if fashion_gan_fids and fashion_vae_fids_list:
        gan_fashion_avg = np.mean(fashion_gan_fids)
        vae_fashion_avg = np.mean(fashion_vae_fids_list)
        ax2.bar(['GAN (avg)', 'VAE (avg)'], [gan_fashion_avg, vae_fashion_avg], 
                color=['#2ca02c', '#d62728'], alpha=0.7)
        ax2.set_ylabel('Average FID Score')
        ax2.set_title('FashionMNIST - Average FID: GAN vs VAE')
        ax2.grid(axis='y', alpha=0.3)
        ax2.text(0, gan_fashion_avg + 0.01, f'{gan_fashion_avg:.3f}', ha='center', va='bottom')
        ax2.text(1, vae_fashion_avg + 0.01, f'{vae_fashion_avg:.3f}', ha='center', va='bottom')
    else:
        ax2.text(0.5, 0.5, 'No data available', ha='center', va='center', transform=ax2.transAxes)
        ax2.set_title('FashionMNIST - Average FID: GAN vs VAE (No Data)')
    
    plt.tight_layout()
    plt.savefig(f"{RESULTS_DIR}/plots/fid_gan_vs_vae.png", dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Saved: {RESULTS_DIR}/plots/fid_gan_vs_vae.png")

if __name__ == "__main__":
    import os
    gan_data, vae_data = parse_report()
    create_plots(gan_data, vae_data)
    print("\nAll plots generated successfully!")

