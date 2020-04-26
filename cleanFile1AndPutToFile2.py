import os


def clean_file1_and_put_to_file2():
    with open("temp_file.txt", "r") as temp_file:
        with open("temp_file2.txt", "w") as temp2_file:

            lookingFor = "€"
            firstTime = True

            for line in temp_file:
                if lookingFor in line:
                    if firstTime:
                        temp2_file.write("-----------------------------------------------\n")
                        firstTime = False

                    temp2_file.write(line)
                    temp2_file.write("-----------------------------------------------\n")
    os.remove("temp_file.txt")
