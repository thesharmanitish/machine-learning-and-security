import pandas as pd

history = pd.DataFrame(
    {
        "user_id": ["u1", "u1", "u1"],
        "ip_prefix": ["1.2.3.*", "5.6.7.8", "98.76.54.*"],
        "login_count": [5, 2, 1],
    }
)


def smoothed_conditional_prob(count, total, alpha=1.0, beta=3.0):
    return (count + alpha) / (total + beta)


user = "u1"
sub = history[history.user_id == user]
total = sub.login_count.sum()

sub = sub.assign(
    p_ip_given_user=sub.login_count.apply(lambda c: smoothed_conditional_prob(c, total))
).sort_values("p_ip_given_user", ascending=False)

print(sub[["ip_prefix", "login_count", "p_ip_given_user"]])
