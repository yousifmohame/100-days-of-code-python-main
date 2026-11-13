# ============ Day 6 ===============

# reeborg

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()
# ==========================
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def skip_wall():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()


# for jump in range(6) :
#     skip_wall()

# ------ while loop ------

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def skip_wall():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while at_goal() != True :
#     skip_wall()
    
# =================
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def skip_wall():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# while at_goal() != True :
#     if front_is_clear() :
#         move()
#     elif wall_in_front() :
#         skip_wall()

# ===================

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():      
#     turn_left()
#     while wall_on_right() :
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear() :
#         move()
#     turn_left()
# while at_goal() != True :
#     if wall_in_front() :
#         jump()
#     else:
#         move()


# =====================

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while not at_goal() :
#     if right_is_clear() and wall_in_front() :
#         turn_right()
#         move()
#     elif front_is_clear() :
#         move()
#     else :
#         turn_left()

#================== english lesson ===================

# what work this man ?
# he work a chef.
# is he a good one ?
# yes, he is.

# def take_step(current_energy):
#     print("Step")
#     return current_energy - 3

# energy = 10
# while energy > 2:
#     energy = take_step(energy)

# print(energy) # will print energy 3 times and final energy value = 1

# def countdown(start_num):
#     while start_num >= 1:
#         print(start_num)
#         start_num -= 1
#     print("Blast off!")
   
# countdown(5)

# What work your brother? 👈 الصح: what is your brother work ?

# He work a software engineer. 👈 الصح : he is works as software engineer.

# اكتب جملتين بالإنجليزية تشرح فيهما الفرق بين متى نستخدم for loop ومتى نستخدم while loop:

# We use a for loop when use lists or ranged tasks

# We use a while loop when we need to make task on time like repeat task every day on 12 am  