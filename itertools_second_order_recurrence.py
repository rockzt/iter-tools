import itertools as it
# For second order recurrence relations such as the fibonacci sequence
# Can be accomplished by using a similar technique as the ons used for first order relations
# There is a slight difference here, you are required to create an intermediate sequence of tuples that keep track
# of the previous two elements of the sequence, and the mao() each of these tuples to their first component to get
# the final sequence

def second_order(p, q ,r, initial_value):
    """Return a sequence defined by s(n) = p*s(n-1) + q*s(n-2) + r."""
    intermediate = it.accumulate(
        it.repeat(initial_value),
        lambda s, _: (s[1], p*s[1] + q*s[0] + r)
    )
    print("Value returned by accumulate (intermediate steps):")
    print(map(lambda x: x[0], intermediate))
    return map(lambda x: x[0], intermediate)

print('Fibonacci sequence :: Second order recurrence relation example')
fbi = second_order(1,1,0,(0,1))
fbi_list = list((next(fbi) for _ in range(5)))
print(fbi_list)  # First 8 Fibonacci numbers


# Now it's time to give a real life example
# Predictive Rate-Limiter (Momentum Based)
"""
Instead of a static ratelimit, you can design an endpoint that predicts
future load based on the last two usage rates and adjusts allowed throughput
dynamically
"""
def second_order(p, q, r, initial_values):
    intermediate = it.accumulate(
        it.repeat(initial_values),
        lambda s, _: (s[1], p*s[1] + q*s[0] + r)
    )
    return map(lambda x: x[0], intermediate)



def get_allowed_request(rate):
    """Get the next allowed request limit based on predicted usage."""
    predictor = second_order( 0.6, 0.3, 5, rate)
    predicted = next(predictor)
    return max(10, min(predicted, 100))  # Clamp between 10 and 100

# Testing the dynamic rate limiter
# Simulated usage rates over time (requests per second)
usage_rates = [10, 15, 20, 25, 30, 35, 40]
# Create tuples of the last two usage rates for prediction
usage_rates_tuples = [tuple(usage_rates[i:i+2]) for i in range(len(usage_rates)-1)]
# Predict allowed requests based on usage rates
allowed_requests = [get_allowed_request(rate_pair) for rate_pair in usage_rates_tuples]
print('Allowed requests based on predicted usage rates:')
print(allowed_requests)