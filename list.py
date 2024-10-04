fruits = ["apple", "banana", "cherry",'orange']
# print(fruits)
fruits.append("mango")
# print(fruits)
fruits.insert(1, "kiwi")
# print(fruits)
fruits.remove("banana")
# print(fruits)
fruits.pop(0)
# print(fruits)

fullname = {"firstname": "John", "lastname": "Doe"}
# print(fullname)

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes  = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

result = convert_seconds(5000)
# print(result)

animals = ["cat", "dog", "rabbit", "guinea pig"]
chars = 0 
for animal in animals:
    chars += len(animal)

# print('Total characters: {}, Average length: {}'.format(chars, chars / len(animals)))    

# winners = ["Messi", "Ronaldo", "Neymar", "Mbappe"]
# for index, person in enumerate(winners):
#     print("{} - {}".format(index + 1, person))
    
# def full_emails(people):
#     result = []
#     for email, name in people:
#         result.append("{}<{}@email.com>".format(name, email))
#     return result

# print(full_emails([("john", "doe"), ("jane", "doe")]))      


# multiples = []

# for x in range(1, 11):
#     multiples.append(x * 7)
    
# print(multiples)    

# languages = ["HTML", "JavaScript", "Python", "Ruby"]
# lengths = [len(language) for language in languages]
# print(lengths)

# my_list = [1,2,3,4,5]
# my_tuple = tuple(my_list)

# print(my_tuple)

# years = ['January 2023', 'March 2023', 'April 2023', 'May 2023', 'October 2025', 'November 2024', 'December 2025']

# updated_years = []

# for year in years:
#     if year.endswith('2023'):
#         new = year.replace('2023', '2024')
#     else:
#         updated_years.append(year)
        
# print(updated_years)            
        

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.


new_filenames = []
for filename in filenames:
    if filename.endswith(".hpp"):
        new = filename.replace(".hpp", ".h")
    else:
        new_filenames.append(filename)
        


# print(new_filenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

# file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
# # for extension in file_counts:
# #     print(extension)
    
# for ext, amount in file_counts.items():
#     print("There are {} files with .{}".format(amount, ext))    
    
# print(file_counts.keys())    
# print(file_counts.values())    
# print(file_counts)
# print(file_counts["txt"])
# print(file_counts["csv"] )

# def count_letter(text):
#     result = {}
#     for letter in text:
#         if letter not in result:
#             result[letter] = 0
#         result[letter] += 1
#     return result


# print(count_letter("hello")  )  
# print(count_letter("tenant") )   
# print(count_letter("a long string with a lot of letters") )   
    
    
# def list_full_names(employee_dictionary):
#     full_names = []
    
#     for last_name, first_names in employee_dictionary.items():
#         for first_name in first_names:
#             full_names.append(first_name + " " + last_name)
#     return(full_names)        

# print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))
        


    

# def invert_resource_dict(resource_dict):
#     new_dictionary = {} 
    
#     for resource_group, resources in resource_dict.items():
#         for resource in resources:
#             if resource in new_dictionary:
#                 new_dictionary[resource].append(resource_group)
#             else:
#                 new_dictionary[resource] = [resource_group]
#     return(new_dictionary)


# print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
#         "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))            


# def sum_server_use_time(Server):
#     total_use_time = 0.0
    
#     for key, value in Server.items():
#         total_use_time += Server[key]
#     return round(total_use_time, 2)    

# FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}

# print(sum_server_use_time(FileServer))

# pet_list = ["Yorkie", "Collie", "Bulldog", "Persian", "Scottish fold", "Siberian"]

# print(pet_list[0:3])

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}

print(wardrobe.update(new_items))