def max_sub_array_of_size_k(k, arr):
  max_sum, window_start, curr_sum = 0, 0, 0

  for window_end in range(len(arr)):
    curr_sum += arr[window_end]   

    if window_end >= k-1:
      max_sum = max(max_sum, sum(arr[window_start-1:window_end]))
      window_start += 1
      curr_sum -= arr[window_start]

  return max_sum