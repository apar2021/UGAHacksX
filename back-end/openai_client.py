import os
from openai import OpenAI
from dotenv import load_dotenv


class OpenAIClient():
    def __init__(self):
        load_dotenv()
        api_key = os.getenv('OPENAI_KEY')
        self.client = OpenAI(api_key=api_key)

    # def get_client(self):
    #     return self.client

    def band_recommendation(self, member, bands):
        bands_str = "\n".join(
            [f"{i + 1}. Band Name is {bands[i]['name']}. {bands[i]['bio']}" for i in range(len(bands))])
        output_format = '{"band_number": band_number, "explanation": explanation}'
        print("OPENAI QUERY")
        content = f"""Here is my bio as a rock band member. {member['bio']}

Here are bios for {len(bands)} rock bands
{bands_str}

Which band would be the best fit for me? Print out the band number with a short explanation of 2-3 sentences. The output should be in the format {output_format}"""
        completion = self.client.chat.completions.create(
            messages=[{
                "role": "user",
                "content": content,
            }],
            model="gpt-4o")
        print("OPENAI QUERY")
        print(content)
        print("OPENAI RESULT")
        print(completion.choices[0].message.content)

    def artist_recommendation(self, band, members):
        members_str = "\n".join(
            [f"{i + 1}. Artist Name is {members[i]['name']}. {members[i]['bio']}" for i in range(len(members))])
        output_format = '{"artist_number": artist_number, "explanation": explanation}'
        print("OPENAI QUERY")
        content = f"""Here is my bio as a rock band. {band['bio']}

Here are bios for {len(members)} rock artists
{members_str}

Which artist would be the best fit for my band? Print out the artist number with a short explanation of 2-3 sentences. The output should be in the format {output_format}"""
        completion = self.client.chat.completions.create(
            messages=[{
                "role": "user",
                "content": content,
            }],
            model="gpt-4o")
        print("OPENAI QUERY")
        print(content)
        print("OPENAI RESULT")
        print(completion.choices[0].message.content)