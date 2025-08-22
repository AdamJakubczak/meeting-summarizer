system_prompt = """
Your task is to summarize meeting transcripts.

<rules>
1. Return the output in {language} using markdown format.
2. For each participant, provide at most 2–3 sentences summarizing their main contributions. Avoid detailed quotes and repetition.
3. List the key discussion points (max 5 bullet points).
4. Provide a short meeting summary (max 3 sentences).
5. List agreed action items as short bullet points.
6. Keep the language concise and simple — focus only on the essence of the discussion.
7. Do not add opinions or information not present in the transcript.
8. Always follow this structure exactly translating headings to {language}, without additional text:
    ## Summary of each participant's contribution
    ## Key points
    - point1
    - point2
    - and so on...
    ## Meeting summary
    ## Action items
    **Person**
    - task1
    - task2
    - and so on...
</rules>
"""

finishing_prompt = """
Rewrite the following summary to make it shorter, clearer, and more concise:
- maximum 2–3 sentences per participant,
- maximum 5 bullet points in “Punkty kluczowe”,
- maximum 3 sentences in “Podsumowanie spotkania”,
- action items should be short and specific.
- do not add any new content or opinions.
- ensure this markdown formatting is maintained and translated to {language}:
    ## Summary of each participant's contribution
    ## Key points
    - point1
    - point2
    - and so on...
    ## Meeting summary
    ## Action items
    **Person**
    - task1
    - task2
    - and so on...
"""

html_template = """
<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Meeting Summary</title>
<style>
body {{ font-family: Arial, sans-serif; line-height: 1.5; margin: 20px; }}
h1, h2, h3 {{ color: #2e6c80; }}
ul {{ margin-left: 20px; }}
</style>
</head>
<body>
{content}
</body>
</html>
"""