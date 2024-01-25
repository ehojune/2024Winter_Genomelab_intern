import matplotlib.pyplot as plt

class D4Z4:
    def __init__(self, pos, XapI, BlnI):
        self.pos = pos
        self.XapI = XapI
        self.BlnI = BlnI

class MatchedReads:
    def __init__(self, pos, d4z4, pLAM, probe, pLAM_seq, read_id):
        self.pos = pos
        self.d4z4 = d4z4
        self.pLAM = pLAM
        self.probe = probe
        self.pLAM_seq = pLAM_seq
        self.read_id = read_id

def draw_arrows(matched_reads):
    # 각 숫자에 적절한 간격을 주기 위한 값
    gap = 700

    # 그림 그리기
    fig, ax = plt.subplots(figsize=(10, 2))

    # 방향 설정
    direction = 1 if matched_reads.pos[0] < matched_reads.pos[1] else -1

    # 검은 화살표 그리기 (일반적인 화살표 모양으로 변경)
    ax.annotate("", xy=(matched_reads.pos[1], 0), xytext=(matched_reads.pos[0], 0),
                arrowprops=dict(arrowstyle='->', color='black', lw=2))
    ax.text((matched_reads.pos[0] + matched_reads.pos[1]) / 2, -0.03, matched_reads.read_id, ha='center', va='bottom', color='black', fontsize=8)
    # 검은 화살표 위에 숫자 표시
    ax.text(matched_reads.pos[0], 0.01, str(matched_reads.pos[0]), ha='center', va='bottom', color='black', fontsize=6)
    ax.text(matched_reads.pos[1], 0.01, str(matched_reads.pos[1]), ha='center', va='bottom', color='black', fontsize=6)

# 실행
if __name__ == "__main__":
  print("Hello, world!")
