
####### Pseudo code #######

# BEGIN
# INPUT: ask the user to input a name in n_word
# INPUT: ask the user to input a verb in v_word
# INPUT: ask the user to input an adjective in a_word
# OUTPUT: output the name, verb and adjective in a short story
        # print(name, "a man of word;yesterday ", verb, "a book called the ",awful, " man")
# END


#### code ####

# enter a given name
n_word = input("Enter a name: ")

# enter a given verb
v_word = input("Enter a verb: ")

# enter a given adjective
a_word = input("Enter an adjective: ")


if n_word != "":
       print(n_word + " " + v_word, " a book called the ", a_word, " world.")   
else:
        # display a story containing the inputs
        print(f''' the world, {v_word} made of humans and the {a_word} thing,\n the {a_word} scenario, {v_word} that whenever you want to change something,\n even if you're the first one to do it,\n you have to start from the beginning.''')






