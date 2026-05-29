import numpy as np
import matplotlib.pyplot as plt

beta_theory = np.linspace(0.01, 89.99, 500)
b = np.deg2rad(beta_theory)
b_pr = np.pi/2 - b

psi_0 = b_pr 
psi_l = 0.5 * np.arccos(np.tanh(np.log(2) + np.arctanh(np.cos(2 * psi_0))))

alpha_theory = np.rad2deg(b_pr - psi_l)
beta_prime_theory = 90 - beta_theory

beta_prime_theory = np.concatenate((-beta_prime_theory, beta_prime_theory[::-1]))
alpha_theory = np.concatenate((-alpha_theory, alpha_theory[::-1]))

geo_chiral_theory = np.sin(2*np.deg2rad(alpha_theory))

fig, ax = plt.subplots(figsize=(7, 5))

ax.plot(beta_prime_theory, geo_chiral_theory, label='Theory', color='steelblue', linewidth=2)
plt.xlim((-60, 60))
ax.set_xlabel(r"$\beta'$ (degrees)", fontsize=13)
ax.set_ylabel(r'$\sin(2\alpha)$', fontsize=13)
ax.set_title('Predicted Chirality For Blade Coating', fontsize=12)
ax.legend(fontsize=11)
ax.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('4d.png', dpi=300)
