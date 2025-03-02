#Function to join given bound_by and tag
def join_middle(bound_by, tag_name):
  # complete the statement below to return the string as required
  x = len(bound_by) // 2
  return bound_by[0:  x] + tag_name + bound_by[x:]


tag_name = "th"
bound_by = "analog"
print(join_middle(tag_name, bound_by))



