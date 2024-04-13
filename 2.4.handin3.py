import numpy as np
from scipy.integrate import quad
import time

S0 = 100
v0 = 0.06
r = 0.05
kappa = 1
theta = 0.06
sigma = 0.3
rho = -0.5
lambda_ = 0.01
tau = 1
K = 100
alpha = 0.3
umax = 50

def characteristicFunctionHeston(u, St, vt, r, kappa, theta, sigma, rho, lambda_, tau, j):
    i = complex(0, 1)
    a = kappa * theta
    b1 = kappa + lambda_ - rho * sigma
    b2 = kappa + lambda_
    u1 = 0.5
    u2 = -0.5

    if j == 1:
        b_j = b1
        u_j = u1
    elif j == 2:
        b_j = b2
        u_j = u2
    else:
        pass

    d_j = np.sqrt((rho * sigma * i * u - b_j) ** 2 - sigma ** 2 * (2 * u_j * i * u - u ** 2))
    g_j = (b_j - rho * sigma * i * u + d_j) / (b_j - rho * sigma * i * u - d_j)
    C_j = r * i * u * tau + (a / sigma ** 2) * ((b_j - rho * sigma * i * u + d_j) * tau - 2 * np.log((1 - g_j * np.exp(d_j * tau)) / (1 - g_j)))
    D_j = ((b_j - rho * sigma * i * u + d_j) / sigma ** 2) * ((1 - np.exp(d_j * tau)) / (1 - g_j * np.exp(d_j * tau)))

    return np.exp(C_j + D_j * vt + i * u * np.log(St))

def priceHestonCallViaCarrMadan(St, vt, r, kappa, theta, sigma, rho, lambda_, tau, K, alpha, umax):
    integrand = lambda u: np.real(
        (np.exp(-complex(0, 1) * u * np.log(K)) * np.exp(-r * tau) *
         characteristicFunctionHeston(u - complex(0, 1) * (alpha + 1), St, vt, r, kappa, theta, sigma, rho, lambda_, tau, 2)) /
        (alpha ** 2 + alpha - u ** 2 + complex(0, 1) * (2 * alpha + 1) * u))
    return (np.exp(-alpha * np.log(K)) / np.pi) * quad(integrand, 0, umax)[0]


start_time = time.time()
option_price = priceHestonCallViaCarrMadan(S0, v0, r, kappa, theta, sigma, rho, lambda_, tau, K, alpha, umax)
end_time = time.time()
computing_time = end_time - start_time

print(f"The option price is (CarrMadan): {option_price}")
print(f"The computing time is (CarrMadan): {computing_time} seconds")
