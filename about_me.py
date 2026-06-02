# Inputs: information needed to complete the profile introduction
first_name = "Jose"
last_name = "Claudio"
age = 31
city = "Orange City"
last_job = "Supply Chain Analyst" #last job is for either current or prior job, in my case is my current job
why_coding = "I am learning coding to advanced my career and solve complex problems through code and AI."
fun_fact = "Gaming is how I unwind... until I start losing."

# We use the inputs to complete the profile in a table like format

# Beginning and header of the table
print("="*40)
print("Student Profile")
print("="*40)
print(f"Name: {first_name} {last_name}") #f-strings helps us use th variables inside the print statements eaier
print(f"Age:  {age}")
print(f"City: {city}")
print(f"Current Career: {last_job}")

print("\n Why I'm learning to code:")
print(why_coding)

print(f"\n Fun Fact: {fun_fact}")

# end of the table
print("="*40)