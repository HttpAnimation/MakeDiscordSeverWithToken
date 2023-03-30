import os 
os.system("pip install discord")
import discord
import asyncio

async def create_server(token):
    client = discord.Client()
    await client.login(token)

    try:
        guild = await client.create_guild("My New Server")
        print(f"Server '{guild.name}' created successfully!")
    except discord.HTTPException as e:
        print(f"Error creating server: {e}")
    finally:
        await client.logout()

async def main():
    token = input("Enter your Discord bot token: ")
    num_servers = int(input("Enter the number of servers you want to create: "))

    for i in range(num_servers):
        await create_server(token)

if __name__ == "__main__":
    asyncio.run(main())
