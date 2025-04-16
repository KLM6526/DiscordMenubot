import discord
from discord.ext import commands
import random

# 봇 기본 설정
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/', intents=intents)

# 점심과 저녁 메뉴 리스트
lunch_menu = [
    "김치찌개", "된장찌개", "비빔밥", "떡볶이",  # 한식
    "짜장면", "짬뽕", "마파두부", "탕수육",      # 중식
    "초밥", "라멘", "우동", "덴푸라",          # 일식
    "피자", "파스타", "햄버거", "샐러드"       # 양식
]

dinner_menu = [
    "삼겹살", "갈비탕", "잡채", "불고기",        # 한식
    "양꼬치", "깐쇼새우", "북경오리", "팔보채",  # 중식
    "스키야키", "카츠돈", "오코노미야키", "나베", # 일식
    "스테이크", "리조또", "치킨윙", "필라프"     # 양식
]

# 슬래시 명령어 등록을 위한 코드 추가
@bot.tree.command(name="메뉴추천", description="점심 또는 저녁 메뉴를 추천합니다.")
async def recommend_menu(interaction: discord.Interaction, time: str):
    if time == "점심":
        menu = random.choice(lunch_menu)
        await interaction.response.send_message(f"오늘 점심 메뉴 추천: {menu} 🍱")
    elif time == "저녁":
        menu = random.choice(dinner_menu)
        await interaction.response.send_message(f"오늘 저녁 메뉴 추천: {menu} 🍽")
    else:
        await interaction.response.send_message("시간을 정확히 입력하세요! (예: 점심, 저녁)")

# 봇 준비 및 명령어 동기화
@bot.event
async def on_ready():
    await bot.tree.sync()  # 슬래시 명령어 동기화
    print(f"봇이 로그인되었습니다: {bot.user}")