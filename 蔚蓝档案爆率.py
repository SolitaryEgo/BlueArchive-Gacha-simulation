# 3星：限定0.7%+常驻2.3%	    31个
# 2星：18.5%	    20个
# 1星：78.5%	    11个

import random
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置中文字体
font_path = "C:\Windows\Fonts\msyh.ttc"  # 请替换为你的中文字体文件路径
font_prop = FontProperties(fname=font_path, size=12)


def draw_card():
    # 每个星级的概率
    prob_3_star = 0.007
    prob_permanent_3_star = 0.023
    prob_2_star = 0.185
    prob_1_star = 0.785

    # 3星角色列表
    three_star_characters = list(range(1, 32))

    # 随机生成一个0到1之间的数，模拟抽卡概率
    draw_result = random.random()

    if draw_result < prob_3_star:
        # 抽中3星角色（限定）
        print(f"抽中3星角色（限定）: {random.choice(three_star_characters)}")
        return "限定3星"
    elif draw_result < prob_3_star + prob_permanent_3_star:
        # 抽中3星角色（常驻）
        print(f"抽中3星角色（常驻）: {random.choice(three_star_characters)}")
        return "常驻3星"
    elif draw_result < prob_3_star + prob_permanent_3_star + prob_2_star:
        # 抽中2星角色
        print(f"抽中2星角色: {random.randint(1, 20)}")
        return "2星"
    else:
        # 抽中1星角色
        print(f"抽中1星角色: {random.randint(1, 11)}")
        return "1星"


# 进行10次抽卡，并统计抽到各星级角色的次数
total_draws = 200
draw_results = {"限定3星": 0, "常驻3星": 0, "2星": 0, "1星": 0}

for _ in range(total_draws):
    result = draw_card()
    draw_results[result] += 1

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 选择一个支持中文的字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 统计结果可视化
labels = list(draw_results.keys())
counts = list(draw_results.values())

plt.bar(labels, counts, color=['red', 'blue', 'green', 'purple'])
plt.xlabel('星级', fontproperties=font_prop)
plt.ylabel('次数', fontproperties=font_prop)
plt.title('抽卡结果统计', fontproperties=font_prop)
plt.show()

# 输出抽到3星角色的次数
three_star_count = draw_results["限定3星"] + draw_results["常驻3星"]
print(f"\n在{total_draws}次抽卡中，你抽到了{three_star_count}个3星角色，其中限定3星次数为{draw_results['限定3星']}，常驻3星次数为{draw_results['常驻3星']}。")
