from quad_func import Quadratic

def accept_input(prompt):
    while True:
        try:
            val = float(input(prompt))
            return val
        except:
            print("Please provide a numeric data.")
            continue
        
def process():
    resp = 'y'
    while resp == 'y' or resp == 'Y':
        answer = ''
        print()
        try:
            segments = []
            values = ["Value A", "Value B", "Value C"]
            for i in range(len(values)):
                question = values[i] + ": "
                prompt = accept_input(question)
                segments.append(prompt)
                
            q = Quadratic(segments[0], segments[1], segments[2])
            answer = q.find_result()
            print()
            print(answer)
            print()
        except:
            print("There was an error with your data entry. Please try again.")
            
        resp = input('Do you wish to continue? (y/n) > ')


print('==================================================================================')
print('=====================  Q U A D R A T I C    E Q U A T I O N  =====================')
print('==================================================================================')
print()
process()