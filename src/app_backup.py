import streamlit as st
from detector import (
    detect_signals,
    calculate_risk_score,
    get_claim_breakdown
)
from knowledge import EXPLANATIONS


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="NiveshLens",
    page_icon="🛡️",
    layout="wide"
)


# =========================================================
# CUSTOM UI
# =========================================================

st.markdown("""
<style>

/* =========================================================
   GLOBAL
   ========================================================= */

.stApp {
    background-color: #f7f9fc !important;
    color: #1f2937 !important;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

p, span, label {
    color: #1f2937;
}

h1, h2, h3, h4, h5, h6 {
    color: #111827 !important;
}


/* =========================================================
   HERO
   ========================================================= */

.hero-title {
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 0px;
    color: #111827 !important;
}

.hero-subtitle {
    font-size: 21px;
    color: #4b5563 !important;
    margin-top: 5px;
}

.badge {
    display: inline-block;
    padding: 6px 14px;
    border-radius: 20px;
    background: #eef2ff !important;
    color: #4338ca !important;
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 12px;
}


/* =========================================================
   SECTION TITLES
   ========================================================= */

.section-title {
    font-size: 25px;
    font-weight: 750;
    margin-top: 10px;
    color: #111827 !important;
}


/* =========================================================
   RISK CARD
   ========================================================= */

.risk-card {
    padding: 18px;
    border-radius: 15px;
    border: 1px solid #d1d5db;
    background: #ffffff !important;
    margin-bottom: 12px;
    color: #1f2937 !important;
}

.risk-card * {
    color: #1f2937 !important;
}

.risk-card-title {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 8px;
    color: #111827 !important;
}


/* =========================================================
   SCORE CARD
   ========================================================= */

.score-card {
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #d1d5db;
    background: #ffffff !important;
    text-align: center;
    margin: 15px 0;
    color: #1f2937 !important;
}

.score-card * {
    color: #1f2937 !important;
}

.score-number {
    font-size: 38px;
    font-weight: 800;
    color: #111827 !important;
}


/* =========================================================
   CLAIM CARD
   ========================================================= */

.claim-card {
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #d1d5db;
    background: #ffffff !important;
    margin-bottom: 15px;
    color: #1f2937 !important;
}

.claim-card * {
    color: #1f2937 !important;
}

.claim-title {
    font-size: 21px;
    font-weight: 700;
    margin-bottom: 12px;
    color: #111827 !important;
}

.claim-label {
    font-weight: 700;
    color: #111827 !important;
}


/* =========================================================
   TEXT AREA
   ========================================================= */

textarea {
    background-color: #ffffff !important;
    color: #111827 !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 10px !important;
}

textarea::placeholder {
    color: #6b7280 !important;
    opacity: 1 !important;
}


/* =========================================================
   DEMO MESSAGE DROPDOWN
   ========================================================= */

/* Main dropdown */
div[data-baseweb="select"] {
    background-color: #ffffff !important;
    color: #111827 !important;
}

/* Dropdown box */
div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
    color: #111827 !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 8px !important;
}

/* Selected value */
div[data-baseweb="select"] span {
    color: #111827 !important;
    background-color: transparent !important;
}

/* Dropdown popup */
div[data-baseweb="popover"] {
    background-color: #ffffff !important;
}

div[data-baseweb="popover"] > div {
    background-color: #ffffff !important;
}

/* Listbox */
div[role="listbox"] {
    background-color: #ffffff !important;
    color: #111827 !important;
    border: 1px solid #d1d5db !important;
}

/* Every option */
div[role="option"] {
    background-color: #ffffff !important;
    color: #111827 !important;
}

/* Option contents */
div[role="option"] * {
    background-color: transparent !important;
    color: #111827 !important;
}

/* Hover */
div[role="option"]:hover {
    background-color: #eef2f7 !important;
    color: #111827 !important;
}

/* Selected option */
div[role="option"][aria-selected="true"] {
    background-color: #eef2f7 !important;
    color: #111827 !important;
}


/* =========================================================
   RADIO BUTTONS
   ========================================================= */

div[data-testid="stRadio"] label {
    color: #1f2937 !important;
}


/* =========================================================
   BUTTONS
   ========================================================= */

.stButton > button {
    background-color: #ffffff !important;
    color: #111827 !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
}

.stButton > button:hover {
    background-color: #f1f5f9 !important;
    color: #111827 !important;
    border-color: #94a3b8 !important;
}

.stButton > button p {
    color: #111827 !important;
}


/* =========================================================
   ALERTS
   ========================================================= */

div[data-testid="stAlert"] {
    color: #1f2937 !important;
}

div[data-testid="stAlert"] p {
    color: #1f2937 !important;
}


/* =========================================================
   CAPTIONS
   ========================================================= */

div[data-testid="stCaptionContainer"] {
    color: #6b7280 !important;
}


/* =========================================================
   CHECKBOX
   ========================================================= */

div[data-testid="stCheckbox"] label {
    color: #1f2937 !important;
}


/* =========================================================
   FILE UPLOADER
   ========================================================= */

section[data-testid="stFileUploaderDropzone"] {
    background-color: #ffffff !important;
    border: 1px dashed #94a3b8 !important;
}

section[data-testid="stFileUploaderDropzone"] * {
    color: #1f2937 !important;
}


/* =========================================================
   FOOTER
   ========================================================= */

.footer {
    text-align: center;
    color: #6b7280 !important;
    font-size: 13px;
    margin-top: 30px;
}


/* =========================================================
   DIVIDER
   ========================================================= */

hr {
    border-color: #e5e7eb !important;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="badge">🛡️ Financial Safety & Content Literacy</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-title">NiveshLens</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">Understand before you act.</div>',
    unsafe_allow_html=True
)

st.write(
    "Analyse financial messages, understand suspicious signals, "
    "and verify information before taking action."
)

st.divider()


# =========================================================
# BHARAT MODE
# =========================================================

st.markdown(
    '<div class="section-title">🌐 Bharat Mode</div>',
    unsafe_allow_html=True
)

language = st.radio(
    "Choose language:",
    ["English", "हिंदी"],
    horizontal=True
)

if language == "English":

    label = "📩 Paste a financial message or claim here:"

    placeholder = (
        "Example:\n"
        "Guaranteed 40% return! Only today! "
        "Send ₹5000 to activate your account."
    )

else:

    label = "📩 यहाँ financial message या claim paste करें:"

    placeholder = (
        "उदाहरण:\n"
        "गारंटीड 40% रिटर्न! सिर्फ आज! "
        "₹5000 भेजें।"
    )


# =========================================================
# DEMO MESSAGE LIBRARY
# =========================================================

st.markdown(
    '<div class="section-title">🧪 Try a Demo Message</div>',
    unsafe_allow_html=True
)

st.caption(
    "Choose a sample message to see how NiveshLens works."
)

demo_messages = {

    "🚨 Guaranteed Return": (
        "URGENT! Guaranteed 40% return with no loss. "
        "Only today! Send ₹5000 to activate your account."
    ),

    "🔐 OTP / Password Request": (
        "Your investment account has been suspended. "
        "Share your OTP and password immediately to reactivate it."
    ),

    "⏰ Urgent Payment": (
        "Limited time opportunity! Act now and transfer ₹3000 "
        "to secure your investment benefits."
    ),

    "🏛️ Authority Claim": (
        "This is an officially approved government investment scheme. "
        "Register today to receive guaranteed benefits."
    ),

    "🇮🇳 Hindi Example": (
        "सिर्फ आज! पक्का मुनाफा और बिना नुकसान। "
        "तुरंत ₹5000 भेजें और अपना अकाउंट एक्टिवेट करें।"
    ),

    "🎁 Fake Reward": (
        "Congratulations! You have won a cash prize of ₹50000. "
        "Click here to claim your reward immediately."
    )
}


selected_demo = st.selectbox(
    "Choose an example:",
    ["-- Select a demo --"] + list(demo_messages.keys())
)


if selected_demo != "-- Select a demo --":

    st.info(
        f"**Demo message:**\n\n"
        f"{demo_messages[selected_demo]}"
    )

    if st.button(
        "📥 Use this message",
        use_container_width=True
    ):

        st.session_state["message_input"] = (
            demo_messages[selected_demo]
        )

        st.success(
            "✅ Demo message loaded into the analysis box!"
        )

        st.rerun()


st.divider()


# =========================================================
# MESSAGE ANALYSIS
# =========================================================

st.markdown(
    '<div class="section-title">💬 Message Analysis</div>',
    unsafe_allow_html=True
)

message = st.text_area(
    label,
    height=180,
    placeholder=placeholder,
    key="message_input"
)


# =========================================================
# ANALYSE MESSAGE
# =========================================================

if st.button(
    "🔍 Analyse Message",
    use_container_width=True
):

    if not message.strip():

        st.warning(
            "Please enter a message first."
        )

    else:

        signals = detect_signals(message)

        risk_score = calculate_risk_score(signals)

        st.divider()


        # =================================================
        # NO SIGNALS
        # =================================================

        if not signals:

            st.success(
                "✅ No predefined risk signals were detected."
            )

            st.info(
                "This does not prove that the message is safe. "
                "Independent verification is still important."
            )


        # =================================================
        # SIGNALS DETECTED
        # =================================================

        else:

            st.error(
                f"🚩 {len(signals)} risk signal(s) detected"
            )


            # =================================================
            # SCORE
            # =================================================

            st.markdown(
                '<div class="section-title">📊 Risk Signal Score</div>',
                unsafe_allow_html=True
            )

            st.progress(risk_score)

            st.markdown(
                f"""
                <div class="score-card">
                    <div class="score-number">
                        {risk_score}/100
                    </div>
                    <div>
                        Detected Risk Signal Score
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )


            # =================================================
            # RISK LEVEL
            # =================================================

            if risk_score <= 20:

                risk_level = "🟢 Low Risk Signals"

                risk_message = (
                    "Only a small number of warning "
                    "patterns were detected."
                )

            elif risk_score <= 50:

                risk_level = "🟠 Moderate Risk Signals"

                risk_message = (
                    "Multiple warning patterns were detected. "
                    "Verify the information before acting."
                )

            elif risk_score <= 75:

                risk_level = "🔴 High Risk Signals"

                risk_message = (
                    "Several strong warning patterns were detected. "
                    "Pause and verify carefully."
                )

            else:

                risk_level = "🚨 Very High Risk Signals"

                risk_message = (
                    "Many strong warning patterns were detected. "
                    "Verify the information independently "
                    "before acting."
                )

            st.info(
                f"**{risk_level}**\n\n"
                f"{risk_message}"
            )


            # =================================================
            # RISK FINGERPRINT
            # =================================================

            st.markdown(
                '<div class="section-title">🧬 Risk Fingerprint</div>',
                unsafe_allow_html=True
            )

            st.caption(
                "These are the suspicious patterns detected "
                "in the message."
            )

            for signal in signals:

                explanation = EXPLANATIONS[signal]

                st.markdown(
                    f"""
                    <div class="risk-card">

                    <div class="risk-card-title">
                    🚩 {signal}
                    </div>

                    <b>💡 Why was this flagged?</b><br>
                    {explanation["why"]}

                    <br><br>

                    <b>🛡️ Safe next step</b><br>
                    {explanation["action"]}

                    </div>
                    """,
                    unsafe_allow_html=True
                )


            # =================================================
            # CLAIM BREAKDOWN
            # =================================================

            st.divider()

            st.markdown(
                '<div class="section-title">🔎 Claim Breakdown</div>',
                unsafe_allow_html=True
            )

            st.caption(
                "NiveshLens breaks the message into claims, "
                "patterns and verification steps."
            )

            claim_breakdown = get_claim_breakdown(signals)

            for item in claim_breakdown:

                st.markdown(
                    f"""
                    <div class="claim-card">

                    <div class="claim-title">
                    🔍 {item["signal"]}
                    </div>

                    <span class="claim-label">
                    📌 Claim:
                    </span><br>
                    {item["claim"]}

                    <br><br>

                    <span class="claim-label">
                    🚩 Detected Pattern:
                    </span><br>
                    {item["pattern"]}

                    <br><br>

                    <span class="claim-label">
                    🔎 What to Verify:
                    </span><br>
                    {item["verify"]}

                    </div>
                    """,
                    unsafe_allow_html=True
                )


            # =================================================
            # SAFETY REMINDER
            # =================================================

            st.divider()

            st.markdown(
                '<div class="section-title">🛡️ Safety Reminder</div>',
                unsafe_allow_html=True
            )

            st.warning(
                "Pause and verify the information through "
                "an appropriate trusted source before taking action."
            )

            st.caption(
                "NiveshLens provides educational risk signals, "
                "not investment recommendations."
            )


            # =================================================
            # THINK BEFORE YOU ACT
            # =================================================

            st.divider()

            st.markdown(
                '<div class="section-title">🛑 Think Before You Act</div>',
                unsafe_allow_html=True
            )

            st.write(
                "Before taking any action, ask yourself:"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.checkbox(
                    "❓ Have I independently verified this claim?",
                    key="verify_claim"
                )

                st.checkbox(
                    "⏰ Am I being pressured to act immediately?",
                    key="urgency_check"
                )

                st.checkbox(
                    "🏛️ Have I verified the authority or organisation mentioned?",
                    key="authority_check"
                )

            with col2:

                st.checkbox(
                    "💰 Do I understand why a payment is being requested?",
                    key="payment_check"
                )

                st.checkbox(
                    "🔐 Am I being asked for sensitive information?",
                    key="credential_check"
                )


# =========================================================
# SCREENSHOT ANALYSIS
# =========================================================

st.divider()

st.markdown(
    '<div class="section-title">📸 Screenshot Analysis</div>',
    unsafe_allow_html=True
)

st.caption(
    "Upload a financial message screenshot and enter "
    "the visible text for analysis."
)

uploaded_image = st.file_uploader(
    "Upload screenshot",
    type=["png", "jpg", "jpeg"]
)

screenshot_text = ""

if uploaded_image:

    st.image(
        uploaded_image,
        caption="Uploaded screenshot",
        use_container_width=True
    )

    screenshot_text = st.text_area(
        "📝 Enter the text visible in the screenshot:",
        height=150,
        placeholder=(
            "Paste or type the text from the screenshot here..."
        )
    )


if st.button(
    "🔍 Analyse Screenshot Text",
    use_container_width=True
):

    if not uploaded_image:

        st.warning(
            "Please upload a screenshot first."
        )

    elif not screenshot_text.strip():

        st.warning(
            "Please enter the text visible in the screenshot."
        )

    else:

        screenshot_signals = detect_signals(
            screenshot_text
        )

        st.divider()

        if not screenshot_signals:

            st.success(
                "✅ No predefined risk signals were detected."
            )

            st.info(
                "This does not prove that the message is safe. "
                "Independent verification is still important."
            )

        else:

            screenshot_score = calculate_risk_score(
                screenshot_signals
            )

            st.markdown(
                '<div class="section-title">'
                '📊 Screenshot Risk Signal Score'
                '</div>',
                unsafe_allow_html=True
            )

            st.progress(screenshot_score)

            st.markdown(
                f"""
                <div class="score-card">
                    <div class="score-number">
                        {screenshot_score}/100
                    </div>
                    <div>
                        Detected Screenshot Risk Signal Score
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                '<div class="section-title">🧬 Risk Fingerprint</div>',
                unsafe_allow_html=True
            )

            for signal in screenshot_signals:

                explanation = EXPLANATIONS[signal]

                st.markdown(
                    f"""
                    <div class="risk-card">

                    <div class="risk-card-title">
                    🚩 {signal}
                    </div>

                    <b>💡 Why was this flagged?</b><br>
                    {explanation["why"]}

                    <br><br>

                    <b>🛡️ Safe next step</b><br>
                    {explanation["action"]}

                    </div>
                    """,
                    unsafe_allow_html=True
                )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div class="footer">

    🛡️ <b>NiveshLens</b> | Educational Risk-Signal Tool<br>

    Built to help users pause, understand suspicious signals,
    and verify information before acting.

    </div>
    """,
    unsafe_allow_html=True
)