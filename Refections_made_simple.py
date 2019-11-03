'''
Refections made simple
======================
Adapted from article
Walker J., Anaesthesia News April 2018 (Issue 369), page 5.
"Refections made simple", Walker J., Anaesthesia News April 2018 (Issue 369), page 5.
some new additions added by me
'''
import random   

# 1st sentence

table01 = ["This was an excellent meeting,", "This was a worthwhile use of my time,", "The event was well organised,", "This activity filled a comprehensive remit,", "This was a good conference,", "A creditworthy meeting,", "A fantastic showcase,", "A pleasurable and productive event,", "A very helpful meeting,", "This opportunity was a positive one,", "A useful exercise,", "This conference was valuable,", "This was an important and eye-opening event,", "This was the first time that I have attended such an event,"]

table02 = ["with many opportunities to network;", "with lots of opportunity to discuss matters with the speakers;", "with a very active social media presence;", "with a nice balance of didactic teaching and open discussion;", "in a well-appointed venue;", "with content that dovetailed neatly with my aspirations;", "in the best traditions of this kind of event;", "given the subject under discussion;", "bearing in mind how previous events such as this have disappointed;", "although the catering was a little lack-lustre;", "with a good balance of clinical and non-clinical subject matter;", "coming as it does at an exciting time in this area;", "with excellent attention to detail in many areas;", "illustrating a novel concept of research;"]

table03 = ["it fulfilled my educational needs", "it validated my current practice", "it helped me to consolidate my existing knowledge base", "it provided much material for reflection", "it covered an interesting range of topics", "it led me to question my thinking", "the Q and A sessions in particular were most informative", "the presentations were of an especially high standard", "the speakers were appropriately challenging", "it was surprisingly stimulating", "the topics were unusually wide-ranging", "its approach was refreshing"]

table04 = ["and highlighted areas for advancement in", "and made me think about the shortfalls within", "but forced me to address the limitations in", "and made me proud of what we've achieved in", "and helped me to develop a more patient-centred paradigm within", "but threw into sharp relief the contrasts within", "and demonstrated the deficiencies in", "and allowed me to appreciate the complexities of", "but left me with no illusions as to the steps needed to improve", "and provided a relaxed forum within which to discuss the needs of", "and underlined the challenges facing", "and may help me address productivity within"]

table05 = ["my Trust.", "my field.", "my department.", "my practice.", "my work.", "my daily activities.", "my specialty.", "my team.", "my group.", "our unit.", "my discipline.", "our current approach.", "our new hospital.", "our educational programme.", "the plans for our new service."]

permutations = len(table01) * len(table02) * len(table03) * len(table04) * len(table05)

print("Struggling to add your own reflections at appraisal?")
print("This is an aid, now with {} permutations!".format(permutations))
print("\n")
print("Here is a sample text:\n")
# main sentence

print(random.choice(table01))
print(random.choice(table02))
print(random.choice(table03))
print(random.choice(table04), end=" ")
print(random.choice(table05))
