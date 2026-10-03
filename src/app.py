
import streamlit as st


from detector import (
    detect_signals,
    calculate_risk_score,
    get_claim_breakdown
)

from knowledge import (
    EXPLANATIONS,
    HINDI_EXPLANATIONS,
    HINDI_SIGNAL_NAMES,
    VERIFICATION_PATHS
)


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="NiveshLens",
    page_icon="🛡️",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* ---------- MAIN APP ---------- */

    .stApp {
        background-color: #f7f9fc !important;
        color: #111827 !important;
    }

    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #111827 !important;
        margin-bottom: 0px;
    }

    .subtitle {
        font-size: 18px;
        color: #6b7280 !important;
        margin-top: 0px;
    }

    .badge {
        display: inline-block;
        padding: 7px 14px;
        border-radius: 20px;
        background-color: #e8f0ff;
        color: #2563eb !important;
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 10px;
    }


    /* ---------- CARDS ---------- */

    .section-card {
        background-color: #ffffff !important;
        color: #111827 !important;
        padding: 22px;
        border-radius: 16px;
        border: 1px solid #e5e7eb;
        margin-bottom: 18px;
    }

    .signal-card {
        background-color: #ffffff !important;
        color: #111827 !important;
        padding: 18px;
        border-radius: 14px;
        border: 1px solid #e5e7eb;
        margin-bottom: 12px;
    }

    .verification-card {
        background-color: #ffffff !important;
        color: #111827 !important;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #dbe4f0;
        margin-bottom: 15px;
    }

    .signal-title {
        font-size: 18px;
        font-weight: 750;
        color: #111827 !important;
        margin-bottom: 8px;
    }

    .small-text {
        font-size: 14px;
        color: #374151 !important;
    }

    .step-text {
        font-size: 15px;
        color: #374151 !important;
        padding: 7px 0px;
    }


    /* =====================================================
       TEXTAREA — WHITE BOX + DARK TEXT
       ===================================================== */

    [data-testid="stTextArea"] {
        background-color: #ffffff !important;
    }

    [data-testid="stTextArea"] > div {
        background-color: #ffffff !important;
    }

    [data-testid="stTextArea"] div[data-baseweb="textarea"] {
        background-color: #ffffff !important;
        border: 1px solid #d1d5db !important;
        border-radius: 10px !important;
    }

    [data-testid="stTextArea"] div[data-baseweb="base-input"] {
        background-color: #ffffff !important;
    }

    [data-testid="stTextArea"] textarea {
        background-color: #ffffff !important;
        color: #111827 !important;
        -webkit-text-fill-color: #111827 !important;
        caret-color: #111827 !important;
        color-scheme: light !important;
        border: none !important;
        outline: none !important;
        box-shadow: none !important;
    }

    [data-testid="stTextArea"] textarea:focus {
        background-color: #ffffff !important;
        color: #111827 !important;
        -webkit-text-fill-color: #111827 !important;
        border: none !important;
        outline: none !important;
        box-shadow: none !important;
    }

    [data-testid="stTextArea"] textarea::placeholder {
        background-color: #ffffff !important;
        color: #6b7280 !important;
        -webkit-text-fill-color: #6b7280 !important;
        opacity: 1 !important;
    }

    [data-testid="stTextArea"] label,
    [data-testid="stTextArea"] label p {
        color: #111827 !important;
    }


    /* ---------- NORMAL STREAMLIT TEXT ---------- */

    .stMarkdown,
    .stMarkdown p,
    .stMarkdown span {
        color: #111827;
    }

    .stCaption,
    .stCaption p {
        color: #6b7280 !important;
    }

    label {
        color: #111827 !important;
    }


    /* ---------- TEXT INPUT ---------- */

    input,
    input:focus {
        background-color: #ffffff !important;
        color: #111827 !important;
        -webkit-text-fill-color: #111827 !important;
        caret-color: #111827 !important;
    }

    input::placeholder {
        color: #6b7280 !important;
        -webkit-text-fill-color: #6b7280 !important;
        opacity: 1 !important;
    }


    /* ---------- SELECTBOX ---------- */

    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #111827 !important;
    }

    div[data-baseweb="select"] span {
        color: #111827 !important;
    }


    /* ---------- RADIO BUTTON ---------- */

    div[data-testid="stRadio"] label {
        color: #111827 !important;
    }

    div[data-testid="stRadio"] p {
        color: #111827 !important;
    }


    /* ---------- FILE UPLOADER ---------- */

    div[data-testid="stFileUploader"] {
        background-color: #ffffff !important;
        border-radius: 12px;
    }

    div[data-testid="stFileUploader"] section {
        background-color: #ffffff !important;
        border: 1px dashed #cbd5e1 !important;
        border-radius: 12px;
    }

    div[data-testid="stFileUploader"] section div {
        color: #111827 !important;
    }

    div[data-testid="stFileUploader"] small {
        color: #6b7280 !important;
    }

    div[data-testid="stFileUploader"] button {
        color: #111827 !important;
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
    }


    /* ---------- BUTTONS ---------- */

    /* Normal Streamlit buttons */
    div.stButton > button,
    button[data-testid="stBaseButton-secondary"] {
        background-color: #ffffff !important;
        color: #111827 !important;
        -webkit-text-fill-color: #111827 !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 10px !important;
    }

    div.stButton > button:hover,
    button[data-testid="stBaseButton-secondary"]:hover {
        background-color: #f8fafc !important;
        color: #111827 !important;
        -webkit-text-fill-color: #111827 !important;
        border-color: #94a3b8 !important;
    }

    div.stButton > button p,
    div.stButton > button span,
    button[data-testid="stBaseButton-secondary"] p,
    button[data-testid="stBaseButton-secondary"] span {
        color: #111827 !important;
        -webkit-text-fill-color: #111827 !important;
    }

    /* Primary buttons */
    div.stButton > button[kind="primary"],
    div.stButton > button[data-testid="stBaseButton-primary"],
    button[data-testid="stBaseButton-primary"] {
        background-color: #2563eb !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        border: 1px solid #2563eb !important;
        border-radius: 10px !important;
    }

    div.stButton > button[kind="primary"] p,
    div.stButton > button[kind="primary"] span,
    div.stButton > button[data-testid="stBaseButton-primary"] p,
    div.stButton > button[data-testid="stBaseButton-primary"] span {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
    }


    /* ---------- ALERTS / WARNING / SUCCESS / ERROR ---------- */

    [data-testid="stAlert"] {
        color: #111827 !important;
    }

    [data-testid="stAlert"] p,
    [data-testid="stAlert"] span,
    [data-testid="stAlert"] div {
        color: #111827 !important;
        -webkit-text-fill-color: #111827 !important;
    }


    /* ---------- METRIC ---------- */

    div[data-testid="stMetric"] {
        background-color: #ffffff !important;
        padding: 12px;
        border-radius: 12px;
    }

    div[data-testid="stMetric"] label {
        color: #6b7280 !important;
    }

    div[data-testid="stMetric"] div {
        color: #111827 !important;
    }


    /* ---------- FOOTER ---------- */

    .footer {
        text-align: center;
        color: #6b7280 !important;
        font-size: 13px;
        padding: 30px 0px 10px 0px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="badge">🛡️ Financial Safety & Content Literacy</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-title">NiveshLens</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Understand before you act.</div>',
    unsafe_allow_html=True
)

st.write("")


# =========================================================
# BHARAT MODE
# =========================================================

language = st.radio(
    "Bharat Mode",
    ["English", "हिंदी"],
    horizontal=True
)

is_hindi = language == "हिंदी"

# =========================================================
# HOW NIVESHLENS WORKS
# =========================================================

st.divider()

st.markdown("### 🔄 How NiveshLens Works")
st.caption(
    "From a suspicious message to a safer verification path."
    if not is_hindi
    else
    "संदिग्ध मैसेज से सुरक्षित verification तक NiveshLens कैसे काम करता है।"
)

flow_cols = st.columns(5)

flow_steps = (
    [
        ("📩", "Input", "Paste a message or upload a screenshot."),
        ("🔍", "Detect", "Find predefined risk signals."),
        ("🧩", "Explain", "Show what the signal means and why it matters."),
        ("🛡️", "Verify", "Give a practical verification path."),
        ("✅", "Pause", "Think before sharing money or sensitive information.")
    ]
    if not is_hindi
    else
    [
        ("📩", "Input", "Message paste करें या screenshot upload करें।"),
        ("🔍", "Detect", "Predefined risk signals पहचानें।"),
        ("🧩", "Explain", "Signal का मतलब और उसका महत्व समझाएँ।"),
        ("🛡️", "Verify", "Practical verification path दें।"),
        ("✅", "Pause", "पैसे या sensitive information देने से पहले रुकें।")
    ]
)

for col, (icon, title, description) in zip(flow_cols, flow_steps):
    with col:
        st.markdown(
            f"""
            <div class="section-card" style="min-height:150px;text-align:center;">
                <div style="font-size:30px;">{icon}</div>
                <div class="signal-title">{title}</div>
                <div class="small-text">{description}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# WHY NIVESHLENS
# =========================================================

st.markdown("### 💡 Why NiveshLens?")

why_cols = st.columns(2)

with why_cols[0]:
    st.markdown(
        """
        <div class="section-card">
            <div class="signal-title">🧠 Explainable, not just a verdict</div>
            <div class="small-text">
                NiveshLens shows the specific risk signals it detected,
                explains why they matter, and connects them to a verification path.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with why_cols[1]:
    st.markdown(
        """
        <div class="section-card">
            <div class="signal-title">🇮🇳 Bharat-first accessibility</div>
            <div class="small-text">
                English and Hindi modes help users understand suspicious
                financial content in a more accessible way.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

why_cols2 = st.columns(2)

with why_cols2[0]:
    st.markdown(
        """
        <div class="section-card">
            <div class="signal-title">🛡️ Safety-focused</div>
            <div class="small-text">
                The system does not tell users what to buy, sell, or invest in.
                It focuses on understanding claims and safer verification.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with why_cols2[1]:
    st.markdown(
        """
        <div class="section-card">
            <div class="signal-title">📱 Message + Screenshot workflow</div>
            <div class="small-text">
                Users can analyze suspicious text directly or start from
                a screenshot and then verify the visible content.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )




# =========================================================
# LANGUAGE VARIABLES
# =========================================================

if is_hindi:

    input_title = "📩 संदिग्ध संदेश जाँचें"

    input_caption = (
        "कोई financial message, WhatsApp message या suspicious text यहाँ paste करें।"
    )

    input_placeholder = (
        "उदाहरण: URGENT! आपको 40% guaranteed return मिलेगा..."
    )

    analyze_button = "🔍 संदेश का विश्लेषण करें"

    demo_title = "🧪 Demo Messages"

    demo_caption = (
        "नीचे दिए गए उदाहरणों में से कोई message चुनकर तुरंत test करें।"
    )

    use_button = "इस संदेश का उपयोग करें"

    analysis_title = "📊 Analysis"

    risk_score_title = "Risk Score"

    risk_fingerprint_title = "🧩 Risk Fingerprint"

    claim_breakdown_title = "📋 Claim Breakdown"

    verification_title = "🧭 सत्यापन का रास्ता"

    verification_caption = (
        "इन कदमों का उपयोग मैसेज के दावों को स्वतंत्र रूप से जाँचने के लिए करें।"
    )

    safety_title = "🛡️ Safety Reminder"

    checklist_title = "✅ Think Before You Act"

    screenshot_title = "📷 Screenshot Analysis"

    screenshot_caption = (
        "Screenshot upload करें और दिखाई देने वाला text नीचे paste करें।"
    )

else:

    input_title = "📩 Check a Suspicious Message"

    input_caption = (
        "Paste a financial message, WhatsApp message or suspicious text here."
    )

    input_placeholder = (
        "Example: URGENT! Guaranteed 40% return with no loss..."
    )

    analyze_button = "🔍 Analyze Message"

    demo_title = "🧪 Demo Messages"

    demo_caption = (
        "Select an example below and test it instantly."
    )

    use_button = "Use this message"

    analysis_title = "📊 Analysis"

    risk_score_title = "Risk Score"

    risk_fingerprint_title = "🧩 Risk Fingerprint"

    claim_breakdown_title = "📋 Claim Breakdown"

    verification_title = "🧭 Verification Path"

    verification_caption = (
        "Use these steps to independently verify the claims before taking action."
    )

    safety_title = "🛡️ Safety Reminder"

    checklist_title = "✅ Think Before You Act"

    screenshot_title = "📷 Screenshot Analysis"

    screenshot_caption = (
        "Upload a screenshot and paste the visible text below."
    )


# =========================================================
# DEMO LIBRARY
# =========================================================

if is_hindi:

    demo_messages = {
        "गारंटीड रिटर्न": (
            "URGENT! आपको 40% गारंटीड रिटर्न मिलेगा और कोई नुकसान नहीं होगा। "
            "सिर्फ आज! अपना अकाउंट activate करने के लिए ₹5000 भेजें।"
        ),

        "OTP / Password Request": (
            "आपका account verify करने के लिए OTP और password भेजें। "
            "अभी verification पूरा करें।"
        ),

        "तुरंत भुगतान": (
            "अभी ₹2500 जमा करें। यह आखिरी मौका है। "
            "आज payment नहीं किया तो आपका benefit बंद हो जाएगा।"
        ),

        "Authority Claim": (
            "यह SEBI approved official scheme है। "
            "सरकार द्वारा मंजूर है। अभी registration करें।"
        ),

        "Fake Reward": (
            "बधाई हो! आपने ₹50,000 cash prize जीता है। "
            "Reward प्राप्त करने के लिए अभी payment करें।"
        ),

        "सामान्य संदेश": (
            "कृपया हमारी financial awareness guide पढ़ें और जानकारी को "
            "स्वतंत्र रूप से verify करें।"
        )
    }

else:

    demo_messages = {
        "Guaranteed Return": (
            "URGENT! Guaranteed 40% return with no loss. "
            "Only today! Send ₹5000 to activate your account."
        ),

        "OTP / Password Request": (
            "Your account needs verification. "
            "Send your OTP and password immediately to complete verification."
        ),

        "Urgent Payment": (
            "Pay ₹2500 immediately. This is your last chance. "
            "Your benefit will expire if payment is not made today."
        ),

        "Authority Claim": (
            "This is a SEBI approved official scheme. "
            "Government approved. Register now."
        ),

        "Fake Reward": (
            "Congratulations! You have won a ₹50,000 cash prize. "
            "Pay now to claim your reward."
        ),

        "Normal Message": (
            "Please read our financial awareness guide and "
            "verify important information independently."
        )
    }


# =========================================================
# DEMO UI
# =========================================================

st.markdown(
    f"### {demo_title}"
)

st.caption(demo_caption)

demo_option = st.selectbox(
    "Select example",
    list(demo_messages.keys())
)

if st.button(use_button):
    st.session_state["message_input"] = demo_messages[demo_option]
    st.rerun()


# =========================================================
# MESSAGE INPUT
# =========================================================

st.markdown(
    f"### {input_title}"
)

st.caption(input_caption)

message = st.text_area(
    "Message",
    value=st.session_state.get("message_input", ""),
    placeholder=input_placeholder,
    height=180,
    label_visibility="collapsed"
)

st.session_state["message_input"] = message


# =========================================================
# ANALYZE MESSAGE
# =========================================================

if st.button(
    analyze_button,
    type="primary",
    use_container_width=True
):

    if not message.strip():

        if is_hindi:
            st.warning("पहले कोई message enter करें.")
        else:
            st.warning("Please enter a message first.")

    else:

        signals = detect_signals(message)

        score = calculate_risk_score(signals)

        breakdown = get_claim_breakdown(signals)

        st.divider()

        st.markdown(
            f"### {analysis_title}"
        )


        # =================================================
        # RISK SCORE
        # =================================================

        st.markdown(
            f"#### 📊 {risk_score_title}"
        )

        st.progress(score / 100)

        col1, col2 = st.columns([1, 3])

        with col1:

            st.metric(
                "Score",
                f"{score}/100"
            )

        with col2:

            if score <= 20:

                if is_hindi:
                    st.success(
                        "कम जोखिम संकेत मिले। फिर भी महत्वपूर्ण जानकारी verify करें।"
                    )
                else:
                    st.success(
                        "Low risk signals detected. Still verify important information."
                    )

            elif score <= 50:

                if is_hindi:
                    st.warning(
                        "कुछ risk signals मिले। आगे बढ़ने से पहले verify करें।"
                    )
                else:
                    st.warning(
                        "Some risk signals detected. Verify before taking action."
                    )

            elif score <= 75:

                if is_hindi:
                    st.warning(
                        "कई risk signals मिले। सावधानी से verify करें।"
                    )
                else:
                    st.warning(
                        "Multiple risk signals detected. Verify carefully before acting."
                    )

            else:

                if is_hindi:
                    st.error(
                        "कई मजबूत risk signals मिले। कार्रवाई करने से पहले स्वतंत्र रूप से verify करें।"
                    )
                else:
                    st.error(
                        "Multiple strong risk signals detected. Verify independently before taking action."
                    )


        # =================================================
        # RISK FINGERPRINT
        # =================================================

        st.divider()

        st.markdown(
            f"### {risk_fingerprint_title}"
        )

        if not signals:

            if is_hindi:

                st.success(
                    "कोई स्पष्ट risk signal detect नहीं हुआ। "
                    "इसका मतलब यह नहीं है कि message निश्चित रूप से सुरक्षित है।"
                )

            else:

                st.success(
                    "No clear risk signal detected. "
                    "This does not mean the message is definitely safe."
                )

        else:

            for signal in signals:

                display_signal = (
                    HINDI_SIGNAL_NAMES.get(signal, signal)
                    if is_hindi
                    else signal
                )

                explanations = (
                    HINDI_EXPLANATIONS
                    if is_hindi
                    else EXPLANATIONS
                )

                info = explanations[signal]

                st.markdown(
                    f'<div class="signal-card"><div class="signal-title">⚠️ {display_signal}</div><div class="small-text"><b>{"क्यों?" if is_hindi else "Why it matters:"}</b> {info["why"]}</div><br><div class="small-text"><b>{"क्या करें?" if is_hindi else "What to do:"}</b> {info["action"]}</div></div>',
                    unsafe_allow_html=True
                )


        # =================================================
        # CLAIM BREAKDOWN
        # =================================================

        st.divider()

        st.markdown(
            f"### {claim_breakdown_title}"
        )

        if not signals:

            if is_hindi:
                st.info(
                    "इस message में कोई predefined risk pattern नहीं मिला।"
                )
            else:
                st.info(
                    "No predefined risk pattern was detected in this message."
                )

        else:

            for item in breakdown:

                signal = item["signal"]

                display_signal = (
                    HINDI_SIGNAL_NAMES.get(signal, signal)
                    if is_hindi
                    else signal
                )

                if is_hindi:

                    hindi_claims = {
                        "Guaranteed Return":
                            "यह संदेश किसी वित्तीय लाभ को गारंटीड या बिना जोखिम वाला बताता है।",

                        "Urgency Pressure":
                            "यह संदेश तुरंत कार्रवाई करने का दबाव बनाता है।",

                        "Authority Claim":
                            "यह संदेश भरोसा पैदा करने के लिए किसी आधिकारिक या सरकारी नाम का उपयोग करता है।",

                        "Payment Request":
                            "यह संदेश आपसे पैसे भेजने या भुगतान करने के लिए कहता है।",

                        "Secretive Language":
                            "यह संदेश जानकारी को दूसरों से छिपाने या गुप्त रखने का दबाव डालता है।",

                        "Credential Request":
                            "यह संदेश OTP, PIN, password या अन्य संवेदनशील जानकारी माँगता है।",

                        "Suspicious Link":
                            "यह संदेश किसी link पर click करने या unverified destination पर जाने के लिए कहता है।",

                        "Fake Reward":
                            "यह संदेश किसी prize, reward या cash benefit को जीतने का दावा करता है।"
                    }

                    hindi_patterns = {
                        "Guaranteed Return":
                            "गारंटीड या बिना जोखिम वाले रिटर्न की भाषा",

                        "Urgency Pressure":
                            "जल्दबाजी या deadline की भाषा",

                        "Authority Claim":
                            "सरकारी या regulatory authority का दावा",

                        "Payment Request":
                            "पैसे भेजने या payment करने का अनुरोध",

                        "Secretive Language":
                            "गोपनीयता या secrecy का दबाव",

                        "Credential Request":
                            "OTP, PIN, password या account information का अनुरोध",

                        "Suspicious Link":
                            "बाहरी link या click-to-verify भाषा",

                        "Fake Reward":
                            "अचानक prize या reward का दावा"
                    }

                    claim = hindi_claims.get(
                        signal,
                        item["claim"]
                    )

                    pattern = hindi_patterns.get(
                        signal,
                        item["pattern"]
                    )

                    verify = "दावे को स्वतंत्र रूप से सत्यापित करें।"

                else:

                    claim = item["claim"]
                    pattern = item["pattern"]
                    verify = item["verify"]

                st.markdown(
                    f'<div class="section-card"><div class="signal-title">🔎 {display_signal}</div><p style="color:#374151 !important;"><b>Claim:</b> {claim}</p><p style="color:#374151 !important;"><b>Detected pattern:</b> {pattern}</p><p style="color:#374151 !important;"><b>Verification:</b> {verify}</p></div>',
                    unsafe_allow_html=True
                )


        # =================================================
        # VERIFICATION PATH
        # =================================================

        st.divider()

        st.markdown(
            f"### {verification_title}"
        )

        st.caption(
            verification_caption
        )

        if signals:

            for signal in signals:

                display_signal = (
                    HINDI_SIGNAL_NAMES.get(signal, signal)
                    if is_hindi
                    else signal
                )

                language_key = "hi" if is_hindi else "en"

                steps = VERIFICATION_PATHS.get(
                    signal,
                    {}
                ).get(
                    language_key,
                    []
                )

                steps_html = "".join(
                    f'<div class="step-text"><b>{index}.</b> {step}</div>'
                    for index, step in enumerate(steps, start=1)
                )

                st.markdown(
                    f'<div class="verification-card"><div class="signal-title">🔎 {display_signal}</div>{steps_html}</div>',
                    unsafe_allow_html=True
                )

        else:

            if is_hindi:

                st.info(
                    "कोई specific verification path trigger नहीं हुआ। "
                    "फिर भी महत्वपूर्ण financial information को independently verify करें।"
                )

            else:

                st.info(
                    "No specific verification path was triggered. "
                    "Still verify important financial information independently."
                )


        # =================================================
        # VERIFICATION CENTER
        # =================================================

        st.divider()

        verification_center_title = (
            "🛡️ Verification Center"
            if not is_hindi
            else "🛡️ Verification Center"
        )

        verification_center_caption = (
            "Turn each detected signal into a specific verification task."
            if not is_hindi
            else "हर detected signal को एक स्पष्ट verification task में बदलें।"
        )

        st.markdown(
            f"### {verification_center_title}"
        )

        st.caption(
            verification_center_caption
        )

        if signals:

            for signal in signals:

                display_signal = (
                    HINDI_SIGNAL_NAMES.get(signal, signal)
                    if is_hindi
                    else signal
                )

                language_key = "hi" if is_hindi else "en"

                steps = VERIFICATION_PATHS.get(
                    signal,
                    {}
                ).get(
                    language_key,
                    []
                )

                if is_hindi:

                    verify_heading = "🔎 इस signal को verify करें"
                    safe_heading = "🛡️ Safe verification"
                    verify_intro = (
                        "इस message पर भरोसा करने से पहले इन बातों को independently check करें:"
                    )

                else:

                    verify_heading = "🔎 Verify this signal"
                    safe_heading = "🛡️ Safe verification"
                    verify_intro = (
                        "Before trusting the message, independently check these points:"
                    )

                with st.container(border=True):

                    st.markdown(
                        f"#### ⚠️ {display_signal}"
                    )

                    st.write(verify_intro)

                    if steps:

                        for index, step in enumerate(
                            steps,
                            start=1
                        ):

                            st.markdown(
                                f"**{index}.** {step}"
                            )

                    st.markdown(
                        f"**{safe_heading}**"
                    )

                    if signal == "Authority Claim":

                        if is_hindi:

                            st.info(
                                "मैसेज में दिए गए link पर निर्भर न करें। संबंधित regulator या organization की official website को independently खोलकर specific claim verify करें।"
                            )

                        else:

                            st.info(
                                "Do not rely on the link inside the message. Open the relevant regulator or organization's official website independently and verify the specific claim."
                            )

                    elif signal == "Credential Request":

                        if is_hindi:

                            st.info(
                                "OTP, PIN, password या authentication code साझा न करें। Request को official channel से verify करें।"
                            )

                        else:

                            st.info(
                                "Do not share OTPs, PINs, passwords, or authentication codes. Verify the request through the organization's official channel."
                            )

                    elif signal == "Payment Request":

                        if is_hindi:

                            st.info(
                                "पैसे भेजने से पहले recipient और payment purpose को independently verify करें।"
                            )

                        else:

                            st.info(
                                "Before sending money, independently verify the recipient and the purpose of the payment."
                            )

                    elif signal == "Suspicious Link":

                        if is_hindi:

                            st.info(
                                "संदिग्ध message के link पर click करने के बजाय official website को manually खोलें।"
                            )

                        else:

                            st.info(
                                "Instead of clicking the message link, open the relevant official website manually."
                            )

                    else:

                        if is_hindi:

                            st.info(
                                "दावे को किसी independent और trusted source से verify करें और pressure में आकर तुरंत action न लें।"
                            )

                        else:

                            st.info(
                                "Verify the claim through an independent and trusted source, and do not act under pressure."
                            )

        else:

            if is_hindi:

                st.info(
                    "कोई specific risk signal detect नहीं हुआ। फिर भी important financial claims को independently verify करें।"
                )

            else:

                st.info(
                    "No specific risk signal was detected. Important financial claims should still be verified independently."
                )


        # =================================================
        # SAFETY REMINDER
        # =================================================

        st.divider()

        st.markdown(
            f"### {safety_title}"
        )

        if is_hindi:

            st.info(
                "NiveshLens आपको यह नहीं बताता कि आपको क्या खरीदना, बेचना या invest करना चाहिए। "
                "इसका उद्देश्य suspicious signals को समझने और information verify करने में मदद करना है."
            )

        else:

            st.info(
                "NiveshLens does not tell you what to buy, sell, or invest in. "
                "Its purpose is to help you understand suspicious signals and verify information."
            )


        # =================================================
        # THINK BEFORE YOU ACT
        # =================================================

        st.divider()

        st.markdown(
            f"### {checklist_title}"
        )

        if is_hindi:

            checklist = [
                "क्या मैंने message के दावे को independently verify किया है?",
                "क्या मुझ पर तुरंत action लेने का pressure बनाया जा रहा है?",
                "क्या मुझसे पैसे या sensitive information माँगी जा रही है?",
                "क्या मैंने message में दिए link के बजाय official source check किया है?"
            ]

        else:

            checklist = [
                "Have I independently verified the claim?",
                "Is the message pressuring me to act immediately?",
                "Is it asking for money or sensitive information?",
                "Did I check an official source instead of trusting the message link?"
            ]

        for item in checklist:

            st.checkbox(item)


# =========================================================
# SCREENSHOT ANALYSIS
# =========================================================

st.divider()

st.markdown(
    f"### {screenshot_title}"
)

st.caption(
    screenshot_caption
)


# ---------- UPLOADER CARD ----------

st.markdown(
    '<div style="background-color:#ffffff;padding:16px;border-radius:14px;border:1px solid #e5e7eb;margin-bottom:10px;"><div style="color:#111827;font-weight:600;font-size:15px;margin-bottom:8px;">📁 Upload your screenshot</div></div>',
    unsafe_allow_html=True
)


uploaded_file = st.file_uploader(
    "Upload screenshot",
    type=["png", "jpg", "jpeg"],
    label_visibility="collapsed"
)


if uploaded_file:

    st.markdown(
        "#### 🖼️ Uploaded Screenshot"
    )

    st.image(
        uploaded_file,
        caption="Uploaded Screenshot",
        use_container_width=True
    )


    # =====================================================
    # SCREENSHOT TEXT INPUT
    # =====================================================

    if is_hindi:

        st.markdown(
            '<div style="color:#111827;font-weight:600;font-size:15px;margin-top:15px;margin-bottom:5px;">📌 Screenshot में दिखाई देने वाला text नीचे paste करें:</div>',
            unsafe_allow_html=True
        )

        screenshot_text = st.text_area(
            "Screenshot Text",
            placeholder="Screenshot का text यहाँ paste करें...",
            height=150,
            key="screenshot_text_hi",
            label_visibility="collapsed"
        )

        screenshot_button = "🔍 Screenshot Text का Analysis करें"

    else:

        st.markdown(
            '<div style="color:#111827;font-weight:600;font-size:15px;margin-top:15px;margin-bottom:5px;">📌 Paste the visible text from the screenshot below:</div>',
            unsafe_allow_html=True
        )

        screenshot_text = st.text_area(
            "Screenshot Text",
            placeholder="Paste the visible screenshot text here...",
            height=150,
            key="screenshot_text_en",
            label_visibility="collapsed"
        )

        screenshot_button = "🔍 Analyze Screenshot Text"


    # =====================================================
    # SCREENSHOT ANALYZE
    # =====================================================

    if st.button(
        screenshot_button,
        use_container_width=True
    ):

        if not screenshot_text.strip():

            if is_hindi:

                st.warning(
                    "Screenshot का text पहले paste करें।"
                )

            else:

                st.warning(
                    "Please paste the visible screenshot text first."
                )

        else:

            screenshot_signals = detect_signals(
                screenshot_text
            )

            screenshot_score = calculate_risk_score(
                screenshot_signals
            )

            st.divider()

            st.markdown(
                "#### 📊 Screenshot Analysis"
            )

            st.progress(
                screenshot_score / 100
            )

            col1, col2 = st.columns([1, 3])

            with col1:

                st.metric(
                    "Risk Score",
                    f"{screenshot_score}/100"
                )

            with col2:

                if screenshot_score <= 20:

                    st.success(
                        "Low risk signals detected."
                    )

                elif screenshot_score <= 50:

                    st.warning(
                        "Some risk signals detected."
                    )

                elif screenshot_score <= 75:

                    st.warning(
                        "Multiple risk signals detected."
                    )

                else:

                    st.error(
                        "Multiple strong risk signals detected."
                    )


            if screenshot_signals:

                st.markdown(
                    f"#### {risk_fingerprint_title}"
                )

                explanations = (
                    HINDI_EXPLANATIONS
                    if is_hindi
                    else EXPLANATIONS
                )

                for signal in screenshot_signals:

                    display_signal = (
                        HINDI_SIGNAL_NAMES.get(signal, signal)
                        if is_hindi
                        else signal
                    )

                    info = explanations[signal]

                    st.markdown(
                        f'<div class="signal-card"><div class="signal-title">⚠️ {display_signal}</div><p style="color:#374151 !important;"><b>{"क्यों?" if is_hindi else "Why:"}</b> {info["why"]}</p><p style="color:#374151 !important;"><b>{"क्या करें?" if is_hindi else "Action:"}</b> {info["action"]}</p></div>',
                        unsafe_allow_html=True
                    )

            else:

                if is_hindi:

                    st.success(
                        "Screenshot text में कोई predefined risk signal detect नहीं हुआ।"
                    )

                else:

                    st.success(
                        "No predefined risk signal detected in the screenshot text."
                    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    '<div class="footer">NiveshLens • Understand before you act.<br>Built for financial safety, misinformation awareness and responsible digital literacy.</div>',
    unsafe_allow_html=True
)