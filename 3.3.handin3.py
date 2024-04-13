import numpy as np
import matplotlib.pyplot as plt
# Setting up plot aesthetics for LaTeX rendering and font settings
plt.rcParams['text.usetex'] = True
plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = 'serif'
plt.rcParams['text.latex.preamble'] = r'\usepackage{amsmath,amssymb,amsfonts,amsthm}'
# Parameters for the model
kappa = 1
sigma = 0.3
delta = 1/(252)
rho = -0.5 
p = 0.5
lambdabar = 0.4 
T = 10
t = np.array([m*delta for m in range(0, (252*T))])
tau = T - t
colors = {
    'sigma': ['blue', 'red', 'green', 'purple'],
    'rho': ['cyan', 'magenta', 'yellow', 'black'],
    'kappa': ['orange', 'grey', 'brown', 'lime'],
    'lambdabar': ['navy', 'teal', 'olive', 'maroon'],
    'p': ['darkgreen', 'darkblue', 'darkred', 'gold', 'violet', 'lightblue'],
    'T': ['Red', 'Blue', 'Green', 'Orange']
}
# Function to calculate the optimal investment strategy
def optimalpi(sigma, rho, lambdabar, p, kappa, tau):
    k0 = (p * lambdabar**2) / (1 - p)
    k1 = kappa - (p * lambdabar * sigma * rho) / (1 - p)
    k2 = sigma**2 + (p * sigma**2 * rho**2) / (1 - p)
    k3 = np.sqrt(k1**2 - k0 * k2)
    b = k0 * (np.exp(k3 * tau) - 1) / (np.exp(k3 * tau) * (k1 + k3) - k1 + k3)
    pi = (lambdabar / (1 - p)) + b * ((sigma * rho) / (1 - p))
    return pi
# Kappa variation plot
fig, ax = plt.subplots(figsize=(5, 3), dpi=300)
ax.set_title("Optimal investment strategy - varying $\\kappa$")
kappa_values = [0.5, 1, 2, 3]
for i, k in enumerate(kappa_values):
    pi_kappa = optimalpi(sigma, rho, lambdabar, p, k, tau)
    ax.plot(t, pi_kappa, color=colors['kappa'][i], label=f"$\\kappa = {k}$")
ax.set_xlabel("Time")
ax.set_ylabel("$\pi^*$")
ax.legend(fontsize=5)
plt.tight_layout()
plt.show()
# Time variation plot
fig, ax = plt.subplots(figsize=(5, 3), dpi=300)
ax.set_title("Optimal investment strategy - varying $T$")
T_values = [5, 10, 30, 100]
for i, T_v in enumerate(T_values):
    t_v = np.array([m*delta for m in range(0, (252*T_v) + 1)])
    tau_v = T_v - t_v
    pi_T = optimalpi(sigma, rho, lambdabar, p, kappa, tau_v)
    ax.plot(t_v, pi_T, color=colors['T'][i], label=f"$T={T_v}$")
ax.set_xlabel("Time")
ax.set_ylabel("$\pi^*$")
ax.legend(fontsize=5)
plt.tight_layout()
plt.show()


# Sigma variation plot
fig, ax = plt.subplots(figsize=(5, 3), dpi=300)
ax.set_title("Optimal investment strategy - varying $\sigma$")
sigma_values = [0.05, 0.3, 0.5, 0.8]
for i, s in enumerate(sigma_values):
    pi_sigma = optimalpi(s, rho, lambdabar, p, kappa, tau)
    ax.plot(t, pi_sigma, color=colors['sigma'][i], label=f"$\sigma = {s}$")
ax.set_xlabel("Time")
ax.set_ylabel("$\pi^*$")
ax.legend(fontsize=5)
plt.tight_layout()
plt.show()

# Rho variation plot
fig, ax = plt.subplots(figsize=(5, 3), dpi=300)
ax.set_title("Optimal investment strategy - varying $\\rho$")
rho_values = [-0.2, -0.5, -0.8, -0.05]
for i, r in enumerate(rho_values):
    pi_rho = optimalpi(sigma, r, lambdabar, p, kappa, tau)
    ax.plot(t, pi_rho, color=colors['rho'][i], label=f"$\\rho = {r}$")
ax.set_xlabel("Time")
ax.set_ylabel("$\pi^*$")
ax.legend(fontsize=5)
plt.tight_layout()
plt.show()



# Lambdabar variation plot
fig, ax = plt.subplots(figsize=(5, 3), dpi=300)
ax.set_title(r"Optimal investment strategy - varying $\bar{\lambda}$")
lambdabar_values = [0.1, 0.4, 0.9, 3]
for i, l in enumerate(lambdabar_values):
    pi_lambdabar = optimalpi(sigma, rho, l, p, kappa, tau)
    ax.plot(t, pi_lambdabar, color=colors['lambdabar'][i], label=rf"$\bar{{\lambda}} = {l}$")
ax.set_xlabel("Time")
ax.set_ylabel(r"$\pi^*$")
ax.set_ylim(0, 7)
ax.set_yticks([1, 2, 3, 4, 5, 6]) 
ax.legend(fontsize=5)
plt.tight_layout()
plt.show()

# p variation plot
fig, ax = plt.subplots(figsize=(5, 3), dpi=300)
ax.set_title("Optimal investment strategy - varying $p$")
p_values = [-5, -2, 0.1, 0.5, 0.8, 0.9]
for i, pv in enumerate(p_values):
    pi_p = optimalpi(sigma, rho, lambdabar, pv, kappa, tau)
    ax.plot(t, pi_p, color=colors['p'][i], label=f"$p = {pv}$")
ax.set_xlabel("Time")
ax.set_ylabel("$\pi^*$")
ax.legend(loc='upper left', fontsize=5)
plt.tight_layout()
plt.show()


