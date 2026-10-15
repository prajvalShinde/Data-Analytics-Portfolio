import numpy as np
from scipy import stats

marks = [75, 80, 85, 70, 90, 78, 82, 88, 76, 84]
hypothesized_mean = 75
alpha = 0.05
n = len(marks)
sample_mean = float(np.mean(marks))
std_dev = float(np.std(marks, ddof=1))
standard_error = std_dev / np.sqrt(n)
t_stat, p_value = stats.ttest_1samp(marks, hypothesized_mean)
t_critical = stats.t.ppf(1 - alpha/2, df=n-1)
margin_of_error = t_critical * standard_error
lower = sample_mean - margin_of_error
upper = sample_mean + margin_of_error
print(f"Sample mean: {sample_mean:.3f}")
print(f"Sample std dev: {std_dev:.3f}")
print(f"Standard error: {standard_error:.3f}")
print(f"t-statistic: {t_stat:.3f}")
print(f"Two-sided p-value: {p_value:.5f}")
print(f"95% margin of error: {margin_of_error:.3f}")
print(f"95% confidence interval: ({lower:.3f}, {upper:.3f})")
print("Reject H0" if p_value < alpha else "Fail to reject H0")
