# https://www.hackerrank.com/contests/ai-ml-module-4-practice-day-1/challenges/b3-sensor-calibrator-min-max-scaling

x, min_v, max_v = map(float, input().split())
norm = ((x-min_v)/(max_v-min_v))
print(f"{norm:.2f}")