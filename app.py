import streamlit as st
import random

# Page config
st.set_page_config(page_title="✨ 제목학원 - 나만의 센스 있는 별명 만들기", layout="centered")

# --- CSS styling: Instagram-like, pastel pink/beige, clean font
st.markdown(
    """
    <style>
    :root{
      --bg1: #ffeef6; /* 연핑크 */
      --bg2: #fff6ea; /* 베이지 */
      --card: rgba(255,255,255,0.7);
      --accent: #ff7ab6;
      --muted: #6b6b6b;
      --title-font: 'Helvetica Neue', Arial, sans-serif;
    }
    html, body, [data-testid='stAppViewContainer']{
      background: linear-gradient(135deg, var(--bg1) 0%, var(--bg2) 100%);
      font-family: var(--title-font);
    }
    .app-card{
      background: var(--card);
      border-radius: 16px;
      padding: 28px;
      box-shadow: 0 6px 18px rgba(0,0,0,0.06);
      max-width: 760px;
      margin: 24px auto;
    }
    .title{font-size:28px; font-weight:700; color:#3b3b3b}
    .subtitle{font-size:14px; color:var(--muted); margin-bottom:18px}
    .result-nick{font-size:26px; font-weight:800; color:#222}
    .fortune{font-size:16px; color:#333}
    .emoji{font-size:28px}
    .small-muted{color:var(--muted); font-size:12px}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("""
<div class="app-card">
  <div class="title">✨ 제목학원 - 나만의 센스 있는 별명 만들기</div>
  <div class="subtitle">유머와 센스가 묻어나는 나만의 이름과 문장 만들기</div>
</div>
""", unsafe_allow_html=True)

with st.container():
    with st.form(key='name_form'):
        st.markdown("""<div style='max-width:760px;margin:0 auto'>""", unsafe_allow_html=True)

        # Required inputs
        key_word = st.text_input('나를 한 단어로 표현한다면?', placeholder='예: 감성, 에너지, 차분함')

        likes_input = st.text_input('내가 좋아하는 것 2가지 (콤마로 구분)', placeholder='예: 초코, 고양이')

        submit = st.form_submit_button('별명 만들기')
        st.markdown("""</div>""", unsafe_allow_html=True)

    # 저장된 변수 이름은 요청대로 `key_word`, `likes`
    # Parse likes into list
    likes = [s.strip() for s in likes_input.split(',') if s.strip()] if likes_input else []

    # Generation logic
    def make_nickname(likes, key_word):
      # key_word 와 좋아하는 것 두 개를 조합해 다양한 유머러스한 별명 생성
      like1 = likes[0] if len(likes) > 0 else None
      like2 = likes[1] if len(likes) > 1 else None

      prefixes = ['달콤한', '은은한', '전설의', '찐', '쫀득한', '감성 충만한', '스웩 넘치는', '핫한', '초월적', '귀염뽀짝한', '시크한', '소울풀한']
      suffixes = ['전설', '요정', '마스터', '왕', '요정님', '러버', '소년', '소녀', '스파크', '천사']

      patterns = []

      # 조합 패턴: 키워드 + 좋아하는 것
      if key_word and like1:
        patterns.extend([
          f"{key_word} {like1}",
          f"{like1} 같은 {key_word}",
          f"{key_word}의 {like1}",
          f"{random.choice(prefixes)} {key_word} {like1}",
          f"{key_word} {like1} {random.choice(suffixes)}",
        ])

      # 좋아하는 것 두 가지 결합
      if like1 and like2:
        patterns.extend([
          f"{like1}×{like2} 혼종",
          f"{like1}의 {like2} 믹스",
          f"{random.choice(prefixes)} {like1}{like2}",
          f"{like1}♡{like2} 매니아",
          f"{like1} & {like2} 스페셜",
          f"{like1}요정 {like2}왕",
        ])

      # 키워드만 있을 때
      if key_word and not like1:
        patterns.extend([
          f"{key_word} 전설",
          f"{random.choice(prefixes)} {key_word}",
          f"{key_word}의 하루",
        ])

      # 기발한 혼성 패턴
      if key_word and like1 and like2:
        patterns.extend([
          f"{key_word}의 {like1}·{like2}",
          f"{like1}{like2}를 닮은 {key_word}",
          f"{random.choice(prefixes)} {like1}의 {key_word}",
        ])

      # 안전한 기본 패턴
      patterns.extend([
        f"{key_word} 스타" if key_word else None,
        f"{random.choice(prefixes)} {like1}" if like1 else None,
        f"{random.choice(prefixes)} {like2}" if like2 else None,
      ])

      # 필터: None 제거
      patterns = [p for p in patterns if p]

      if not patterns:
        return '센스쟁이'

      nick = random.choice(patterns)
      return nick

    def make_fortune(nick):
      templates = [
        f"너에게 딱 맞는 별명은 {nick}. 이미 전설의 시작이야 ✨",
        f"별명 '{nick}'으로 시작하는 순간, 너의 매력이 파도처럼 밀려온다 🌊",
        f"'{nick}'으로 불릴 때마다, 주변이 웃음으로 가득 찬다 😎",
        f"오늘부터 넌 '{nick}'. 모두가 너의 센스를 리트윗할 거야 🎉",
        f"별명 '{nick}'은 네 장점을 한 문장으로 요약한 표현이야. 굿 초이스! 🌈",
        f"'{nick}'으로 불리면, 소소한 순간도 멋진 에피소드로 변한다 ✨",
        f"그 별명, 이미 예약완료야 — '{nick}'의 하루가 기대돼 🎈",
      ]
      return random.choice(templates)

    # 결과 출력
    if submit:
      nickname = make_nickname(likes, key_word)
        fortune = make_fortune(nickname)

        st.markdown(
            f"""
            <div class='app-card' style='text-align:center'>
              <div class='emoji'>🎉</div>
              <div class='result-nick'>🎉 너의 별명은 '<span style='color:#ff4d94'>{nickname}</span>' 🎉</div>
              <div style='height:8px'></div>
              <div class='fortune'>🌟 {fortune}</div>
              <div style='height:12px'></div>
              <div class='small-muted'>Tip: 더 다양한 조합을 원하면 좋아하는 것을 바꿔보세요.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        # 초기 안내 카드
        st.markdown(
            """
            <div class='app-card'>
              <div style='font-weight:700; color:#3b3b3b'>시작해볼까요? ✨</div>
              <div class='small-muted' style='margin-top:8px'>위 입력란에 간단히 입력한 뒤 '별명 만들기'를 눌러보세요. 예시: 좋아하는 것 → 초코, 고양이</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Footer: run & deploy instructions
    st.markdown("""
    <div style='max-width:760px;margin:18px auto;padding:12px 18px;border-radius:12px;background:rgba(255,255,255,0.55)'>
      <div style='font-size:13px;color:#555'><strong>실행 방법</strong></div>
      <div style='font-size:13px;color:#444;margin-top:6px'>로컬에서 실행: <code>streamlit run app.py</code></div>
      <div style='font-size:13px;color:#444;margin-top:6px'>배포: GitHub에 푸시 후 Streamlit Cloud에 연결하여 배포하세요.</div>
    </div>
    """, unsafe_allow_html=True)
