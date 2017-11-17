question_template = {
    "title": "default title",
    "question": "default question",
    "answer": "default answer",
    "hints": []
    }


def make_new_question(title, question, answer, hints=None):
    new_question = question_template.copy()
    new_question["title"] = title
    new_question["question"] = question
    new_question["answer"] = answer
    if hints is not None:
        new_question["hints"].extend(hints)
        
        #new_question["hints"] = hints
    
    return new_question


question_1 = make_new_question("title1", "question1", "answer1", ["q1 hint1", "q1 hint2"])
question_2 = make_new_question("title2", "question2", "answer2")
question_3 = make_new_question("title3", "question3", "answer3", ["q3 hint1"])


'''
Things start going wrong after question 1. Let's look at question 2 and see what we got:

  {
    "title": "title2",
    "question": "question2",
    "answer": "answer2",
    "hints": ["q1 hint1", "q1 hint2"]
}
Python
Question 2 wasn't supposed to have any hints! And question 3 is even more jumbled:

  {
    "title": "title3",
    "question": "question3",
    "answer": "answer3",
    "hints": ["q1 hint1", "q1 hint2", "q3 hint1"]
}

It has hints from question 1 and its own hints! What's going on here?

The problem all stems from how we used our question_template—there's nothing wrong with the template itself, but when we call question_template.copy(), we're making a shallow copy of our dictionary. A shallow copy basically does this:

  def shallow_copy(original_dict):
    new_dict = {}

    for key, value in original_dict.items():
        new_dict[key] = value

    return new_dict

All of the items, keys and values, refer to the exact same objects after making a shallow copy. The issue arises with our hints because it's a list, which is mutable. Our copy of question_template points to the same exact object as the hints in our template! We can see this if we just print out our template:

  question_template = {
    "title": "default title",
    "question": "default question",
    "answer": "default answer",
    "hints": ["q1 hint1", "q1 hint2", "q3 hint1"]
}
Python
One way around this problem would be to overwrite the list of hints every time:

  def make_new_question(title, question, answer, hints=None):
    new_q = question_template.copy()
    new_q["title"] = title
    new_q["question"] = question
    new_q["answer"] = answer

    if hints is not None:

        # overwrite the mutable hints default here
        new_q["hints"] = hints

    return new_q
    
    A more general solution is to ensure that any mutable objects have true copies created, rather than just passing along a "reference" to the original object. And if that mutable object is a container, then any of its mutable elements need to make true copies, and so on, recursively. Rolling this code by hand would be error-prone and tedious—luckily, Python has a standard library function that can help: deepcopy().

We can just drop that in where our shallow copy was:

  from copy import deepcopy

def make_new_question(title, question, answer, hints=None):

    # make a deep copy before doing anything else
    new_q = deepcopy(question_template)
    new_q["title"] = title
    new_q["question"] = question
    new_q["answer"] = answer

    if hints is not None:
        new_q["hints"].extend(hints)

    return new_q

Now, the list of hints in each new question will be a brand new list, so changes to it won't affect other questions or the template question.

'''