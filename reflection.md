# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
The following was broken when I started
1. The hints were wrong. It said go lower when I put 1. It should not accept 1.
2. The game allowed me to submit 0 when the only allowed guess was 1-100, and the hint even said go lower at 0.
3. It told me out of attempts and gave the answer even though I still had 1 attempt left.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|guess of 1 | Put a number between 1 and 100 "Go lower" hint shown| none|
|Guess of 0 | Put a number between 1-100 | "Go lower" hitn shown| none|
| guess of 51| Go higher, 1 attempt left| "Go lower" hint shown|Out of attempts |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
chat agent in VScode
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
AI suggested adding a check to validate the guess was within expected range. 
The suggestion was correct. 
To verify I told it to generate a pytest in test_game_logic.py to confirm the hint logic is right. The test passed. I also ran the app.py and tested myself, then found out that when I put 100, the hint logic was broken because it was treating the guess input as a string instead of type casting to int before doing the check logic fo rthe hint.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
WHile tryiyng to tell AI to update code to validate the guess input as a valid input, it started applying changes to a different function in app.py. 
I had to click undo to reject the suggestion and give it a more specific prompt and the specific function to update. 
Then I told it to generate a pytest in test_game_logic.py to test the hint logic when putting the maximum guess number and the test passed. Then I tested it by running the app.py and the hint logic was right when the max guess number was not the secret number.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I ran the game and tested the code myself to target the specific bug
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I put 100 as a guess and the hint said Go higher. It showe dme that even after AI corrected the hint logic, it still broke in certain instances, It revealed that I still was not typecasting my input to int before doing a check to see if it was a valid guess.
- Did AI help you design or understand any tests? How?
Yes, it explained the test it was adding. It also gave valid suggestions when I explained the bug I had discovered while playing the game.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Simply refresh the webpage after editing your code and it should reflect the recent code changes. Also, as long as it's still running in vs code in virtual environemnt you should be able to play your game app
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
Testing the code myself even after AI has generated pytests
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task? 
Be more specific with the functions i wnat to edit and prompting in general.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
ALways verify and test. Also, understand the app so that you can tell if AI is giving the right suggetsion or has the right logic. This way you know when to reject AI code suggestion. 
