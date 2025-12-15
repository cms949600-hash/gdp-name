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

        likes_input = st.text_input('내가 좋아하는 것 3가지 (콤마로 구분)', placeholder='예: 초코, 고양이, 꽃')

        mood = st.selectbox('내가 원하는 감성', options=['유쾌한', '감성적인', '힙한', '귀여운', '쿨한'])

        submit = st.form_submit_button('별명 만들기')
        st.markdown("""</div>""", unsafe_allow_html=True)

    # 저장된 변수 이름은 요청대로 `key_word`, `likes`, `mood`
    # Parse likes into list
    likes = [s.strip() for s in likes_input.split(',') if s.strip()] if likes_input else []

    # Generation logic
    def make_nickname(mood, likes, key_word):
      # 다양한 별명 패턴을 랜덤으로 선택하여 좀 더 창의적인 별명 생성
      first_like = likes[0] if len(likes) > 0 else None
      patterns = []
      if first_like:
        patterns.extend([
          f"{mood} {first_like}",
          f"{first_like}의 {mood}",
          f"{mood}한 {first_like}",
          f"{first_like} 요정 ({mood})",
          f"{mood} {first_like}★",
        ])
      if key_word:
        patterns.extend([
          f"{mood} {key_word}",
          f"{key_word} 같은 {mood}",
          f"{key_word}의 {mood} 스타일",
        ])

      # 기본 패턴
      patterns.extend([
        f"{mood} 스타",
        f"{mood} 전설",
        f"{mood} 빛나는 존재",
      ])

      nick = random.choice(patterns)
      return nick

    def make_fortune(nick):
      templates = [
        f"너에게 딱 맞는 별명은 {nick}. 이미 전설의 시작이야 ✨",
        f"별명 '{nick}'으로 시작하는 순간, 너의 감성이 모두를 사로잡는다 🌟",
        f"'{nick}'으로 불리는 날부터, 주변에 웃음이 번지기 시작한다 😎",
        f"오늘부터 넌 '{nick}'. 작은 행동이 큰 센스를 만든다 🎉",
        f"별명 '{nick}'은 네가 가진 매력을 잘 설명해준다. 굿 초이스! 🌈",
        f"'{nick}'으로 불릴 때마다, 너의 하루가 반짝인다 ✨",
      ]
      return random.choice(templates)

    # 결과 출력
    if submit:
        nickname = make_nickname(mood, likes, key_word)
        fortune = make_fortune(nickname)

        st.markdown(
            f"""
            <div class='app-card' style='text-align:center'>
              <div class='emoji'>🎉</div>
              <div class='result-nick'>🎉 너의 별명은 '<span style='color:#ff4d94'>{nickname}</span>' 🎉</div>
              <div style='height:8px'></div>
              <div class='fortune'>🌟 {fortune}</div>
              <div style='height:12px'></div>
              <div class='small-muted'>Tip: 더 다양한 조합을 원하면 좋아하는 것이나 감성을 바꿔보세요.</div>
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
              <div class='small-muted' style='margin-top:8px'>위 입력란에 간단히 입력한 뒤 '별명 만들기'를 눌러보세요. 예시: 좋아하는 것 → 초코, 고양이, 꽃</div>
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
