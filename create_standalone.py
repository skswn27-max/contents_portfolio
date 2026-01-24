import base64
import os

def encode_image(path):
    if not os.path.exists(path):
        print(f"NOT FOUND: {path}")
        return ""
    with open(path, "rb") as f:
        data = f.read()
    ext = path.split(".")[-1].lower()
    if ext == "jpg":
        ext = "jpeg"
    return f"data:image/{ext};base64,{base64.b64encode(data).decode('utf-8')}"

# Encode all images
print("Encoding images...")
images = {
    "profile": encode_image("images/이난주_프로필사진.JPG"),
    "p1_1": encode_image("images/프로젝트 1_1번 이미지.jpeg"),
    "p1_2": encode_image("images/프로젝트 1_2번 이미지.jpg"),
    "p1_3": encode_image("images/프로젝트1_3번 이미지.jpg"),
    "p2_1": encode_image("images/프로젝트 2_1번 이미지.jpeg"),
    "p2_2": encode_image("images/프로젝트 2_2번 이미지.jpg"),
    "p2_3": encode_image("images/프로젝트 2_3번 이미지.jpeg"),
    "p3_1": encode_image("images/프로젝트 3_1번 이미지.jpeg"),
    "p3_2": encode_image("images/프로젝트 3_3번 이미지.jpeg"),
    "p4_1": encode_image("images/프로젝트 4_1번 이미지.jpeg"),
    "p4_2": encode_image("images/프로젝트 4_2번 이미지.jpg"),
    "p5_1": encode_image("images/프로젝트 5_1번 이미지.jpeg"),
    "p5_2": encode_image("images/프로젝트 5_2번 이미지.jpeg"),
    "p5_3": encode_image("images/프로젝트 5_3번 이미지.jpg"),
    "dashboard": encode_image("images/Sample Dashboard.png"),
}
print("Images encoded!")

html_template = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Brand Maker : 이난주 | IMC 브랜드 마케터 포트폴리오</title>
    <style>
:root { --accent: #0066FF; }
.hl-yellow { font-weight: 700; color: #000; }
.hl-green { font-weight: 700; color: #0066FF; }
.skill-highlight { font-weight: 700; color: #0066FF; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans KR", sans-serif; font-size: 14px; line-height: 1.7; color: #000; background: #fff; }
.container { max-width: 900px; margin: 0 auto; padding: 0 40px; }
.hero { padding: 80px 40px; background: #000; text-align: center; }
.hero-title { font-size: 2.5rem; font-weight: 700; color: #fff; margin-bottom: 16px; }
.hero-title .korean { display: block; margin-top: 8px; }
.hero-tagline { font-size: 0.75rem; color: rgba(255,255,255,0.6); letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 12px; padding-bottom: 12px; border-bottom: 1px solid rgba(255,255,255,0.2); display: inline-block; }
.hero-sub { font-size: 0.85rem; color: rgba(255,255,255,0.5); }
.toc { padding: 60px 0; background: #FAFAFA; }
.toc-title { font-size: 1.8rem; font-weight: 700; margin-bottom: 32px; }
.toc-grid { display: flex; flex-direction: column; }
.toc-item { display: flex; align-items: center; gap: 20px; padding: 16px 0; border-bottom: 1px solid rgba(0,0,0,0.1); }
.toc-item:first-child { border-top: 1px solid rgba(0,0,0,0.1); }
.toc-number { font-size: 0.8rem; font-weight: 600; color: #888; width: 30px; }
.toc-name { font-size: 1rem; font-weight: 600; flex: 1; }
.toc-category { font-size: 0.75rem; color: #888; }
section { padding: 60px 0; }
.section-label { font-size: 0.7rem; color: #888; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 16px; }
.section-title { font-size: 1.8rem; font-weight: 600; margin-bottom: 40px; }
.about { background: #fff; border-top: 1px solid rgba(0,0,0,0.1); }
.about-intro h2 { font-size: 1.6rem; font-weight: 700; line-height: 1.5; margin-bottom: 16px; }
.about-intro .highlight { border-bottom: 2px solid #0066FF; padding-bottom: 2px; }
.about-description { font-size: 0.95rem; color: #555; line-height: 1.8; }
.about-stats { display: flex; gap: 40px; margin-top: 24px; padding-top: 24px; border-top: 1px solid rgba(0,0,0,0.1); flex-wrap: wrap; }
.stat-item { border-left: 2px solid #000; padding-left: 16px; }
.stat-number { display: block; font-size: 1.8rem; font-weight: 700; }
.stat-label { font-size: 0.75rem; color: #888; }
.capabilities { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin-top: 32px; }
.capability-item { display: flex; gap: 16px; padding: 20px; border: 1px solid rgba(0,0,0,0.1); }
.capability-number { font-size: 0.7rem; font-weight: 600; }
.capability-content h4 { font-size: 0.95rem; font-weight: 600; margin-bottom: 6px; }
.capability-content p { font-size: 0.85rem; color: #555; line-height: 1.5; }
.work { background: #FAFAFA; border-top: 1px solid rgba(0,0,0,0.1); }
.projects-list { display: flex; flex-direction: column; gap: 60px; }
.project-item { padding-bottom: 40px; border-bottom: 1px solid rgba(0,0,0,0.1); page-break-inside: avoid; }
.project-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px; flex-wrap: wrap; gap: 8px; }
.project-index { font-size: 0.8rem; font-weight: 700; }
.project-meta { display: flex; flex-direction: column; gap: 4px; align-items: flex-end; }
.project-category { font-size: 0.7rem; color: #888; letter-spacing: 0.08em; text-transform: uppercase; }
.project-period { font-size: 0.7rem; color: #888; }
.project-contribution { font-size: 0.65rem; color: rgba(25,25,25,0.75); background: rgba(255,255,255,0.75); border: 1px solid rgba(0,0,0,0.06); padding: 6px 8px; border-radius: 8px; }
.project-name { font-size: 1.4rem; font-weight: 700; margin-bottom: 12px; }
.project-summary { font-size: 0.9rem; color: #555; line-height: 1.6; margin-bottom: 24px; }
.project-strengths { margin: 12px 0 20px; }
.chips { display: flex; flex-wrap: wrap; gap: 8px; }
.chip { display: inline-flex; padding: 6px 12px; border: 1px solid rgba(0,0,0,0.2); font-size: 0.7rem; font-weight: 500; }
.project-media { margin-bottom: 24px; }
.media-grid-thumbs { display: flex; gap: 12px; flex-wrap: wrap; justify-content: center; }
.media-thumb { width: 140px; border: 1px solid rgba(0,0,0,0.1); }
.media-thumb img { width: 100%; height: auto; display: block; }
.project-main-image { margin: 16px 0 24px; border: 1px solid rgba(0,0,0,0.1); }
.project-main-image img { width: 100%; height: auto; display: block; }
.project-details-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; }
.detail-card { padding: 20px; background: #fff; border: 1px solid rgba(0,0,0,0.1); }
.detail-card.role { grid-column: 1 / -1; }
.detail-label { display: block; font-size: 0.75rem; font-weight: 600; margin-bottom: 12px; }
.detail-card ul { list-style: none; display: flex; flex-direction: column; gap: 8px; }
.detail-card li { font-size: 0.8rem; color: #555; padding-left: 12px; position: relative; line-height: 1.5; }
.detail-card li::before { content: '•'; position: absolute; left: 0; color: #888; }
.detail-card p { font-size: 0.8rem; color: #555; line-height: 1.5; margin: 0; }
.insight-quote { margin: 0 0 12px 0; padding: 14px 18px; background: #FAFAFA; border-left: 3px solid #000; font-size: 0.85rem; font-weight: 600; }
.result-metrics { display: flex; gap: 12px; flex-wrap: wrap; }
.metric { flex: 1; min-width: 80px; text-align: center; padding: 16px 12px; background: #FAFAFA; }
.metric-value { display: block; font-size: 1.2rem; font-weight: 700; margin-bottom: 4px; }
.metric-label { font-size: 0.65rem; color: #888; }
.result-qual { margin-top: 12px; padding-top: 12px; border-top: 1px dashed rgba(0,0,0,0.12); }
.result-qual ul { list-style: none; display: grid; gap: 6px; }
.result-qual li { color: #555; padding-left: 12px; position: relative; font-size: 0.8rem; }
.result-qual li::before { content: '•'; position: absolute; left: 0; color: #888; }
.skills { background: #fff; border-top: 1px solid rgba(0,0,0,0.1); }
.skills-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }
.skill-block h4 { font-size: 0.9rem; font-weight: 600; margin-bottom: 12px; }
.skill-block ul { list-style: none; display: flex; flex-direction: column; gap: 8px; }
.skill-block li { font-size: 0.8rem; color: #555; padding-left: 12px; position: relative; }
.skill-block li::before { content: ''; position: absolute; left: 0; top: 50%; transform: translateY(-50%); width: 4px; height: 4px; background: #000; }
.contact { background: #FAFAFA; border-top: 1px solid rgba(0,0,0,0.1); }
.contact-wrapper { display: flex; justify-content: flex-start; align-items: center; gap: 60px; flex-wrap: wrap; }
.contact-content { flex: 1; max-width: 500px; min-width: 280px; }
.contact-title { font-size: 2rem; font-weight: 700; margin-bottom: 16px; line-height: 1.2; }
.contact-description { font-size: 0.95rem; color: #555; margin-bottom: 32px; line-height: 1.7; }
.contact-links { display: flex; flex-direction: column; gap: 16px; }
.contact-link { display: flex; flex-direction: column; gap: 4px; text-decoration: none; padding: 20px; background: #fff; border: 1px solid rgba(0,0,0,0.1); }
.link-label { font-size: 0.7rem; color: #888; letter-spacing: 0.08em; text-transform: uppercase; }
.link-value { font-size: 0.95rem; color: #000; font-weight: 500; }
.contact-profile { flex-shrink: 0; }
.profile-image-wrapper { width: 200px; }
.profile-image-wrapper img { width: 100%; height: auto; display: block; }
.footer { padding: 30px 0; border-top: 1px solid rgba(0,0,0,0.1); text-align: center; background: #fff; }
.footer p { font-size: 0.8rem; color: #888; }
@media print { body { font-size: 11px; } .hero { padding: 40px 20px; } .hero-title { font-size: 1.8rem; } section { padding: 30px 0; } .container { padding: 0 20px; } .project-item { page-break-inside: avoid; } .skills-grid { grid-template-columns: repeat(2, 1fr); } .capabilities { grid-template-columns: 1fr; } .project-details-grid { grid-template-columns: 1fr; } }
@media (max-width: 768px) { .skills-grid { grid-template-columns: repeat(2, 1fr); } .capabilities { grid-template-columns: 1fr; } .project-details-grid { grid-template-columns: 1fr; } .about-stats { flex-direction: column; gap: 16px; } }
    </style>
</head>
<body>
    <section class="hero"><div class="hero-content"><h1 class="hero-title">Brand Maker : <span class="korean">이난주</span></h1><p class="hero-tagline">CONTENTS · DATA-BASED STRATEGY · AI</p><p class="hero-sub">F&F · 브랜드 마케팅 · 4년+</p></div></section>

    <section class="toc"><div class="container"><div class="section-label">CONTENTS</div><h2 class="toc-title">주요 프로젝트</h2><div class="toc-grid">
        <div class="toc-item"><span class="toc-number">01</span><span class="toc-name">듀베티카 24FW 셀럽/인플루언서 협업</span><span class="toc-category">셀럽 · IMC · PM</span></div>
        <div class="toc-item"><span class="toc-number">02</span><span class="toc-name">세르지오 타키니 한남 플래그십 & 콜라보</span><span class="toc-category">Flagship · Collaboration</span></div>
        <div class="toc-item"><span class="toc-number">03</span><span class="toc-name">현대카드 슈퍼매치</span><span class="toc-category">Sponsorship</span></div>
        <div class="toc-item"><span class="toc-number">04</span><span class="toc-name">세르지오 타키니 EQL 성수 팝업</span><span class="toc-category">Retail Pop-up</span></div>
        <div class="toc-item"><span class="toc-number">05</span><span class="toc-name">몬테카를로 마스터즈 MCCC 글로벌 행사</span><span class="toc-category">Global Event</span></div>
        <div class="toc-item"><span class="toc-number">06</span><span class="toc-name">시즌 IMC 전략 수립</span><span class="toc-category">Strategy</span></div>
        <div class="toc-item"><span class="toc-number">07</span><span class="toc-name">AI Agent MKT KPI 대시보드 구축</span><span class="toc-category">AI · Automation</span></div>
    </div></div></section>

    <section class="about"><div class="container"><div class="section-label">ABOUT</div><div class="about-content"><div class="about-intro"><h2><span class="highlight">뉴미디어 채널과 콘텐츠</span>로<br>브랜드를 성장시키는 IMC 마케터</h2><p class="about-description">패션 브랜드에서 4년간 <span class="hl-yellow">브랜딩과 매출, 두 마리 토끼</span>를 잡아왔어요. 숫자로 설득하고, 감각으로 마무리하는 스타일이에요. 혼자 빛나는 것보다 <span class="hl-green">팀이 같이 달릴 때 더 멀리 간다</span>고 생각해요.</p></div><div class="about-stats"><div class="stat-item"><span class="stat-number">4+</span><span class="stat-label">Years at F&F</span></div><div class="stat-item"><span class="stat-number">500만</span><span class="stat-label">Max Contents View</span></div><div class="stat-item"><span class="stat-number">손익분기점 달성</span><span class="stat-label">신규 브랜드</span></div></div></div>
    <div class="capabilities">
        <div class="capability-item"><div class="capability-number">01</div><div class="capability-content"><h4>IMC 전략 & 브랜드 성장</h4><p>SNS, PR, 셀럽, 팝업, 광고를 <span class="hl-yellow">하나의 메시지</span>로 엮어요. 6개월 만에 <span class="hl-green">인지도·매출 2배</span>.</p></div></div>
        <div class="capability-item"><div class="capability-number">02</div><div class="capability-content"><h4>경쟁사 데이터 기반 전략</h4><p>브랜딩 계획 전 <span class="hl-yellow">경쟁사 데이터를 꼼꼼히</span> 분석해요. 시장 포지셔닝과 차별화 포인트를 <span class="hl-green">숫자로 검증</span>하고 실행해요.</p></div></div>
        <div class="capability-item"><div class="capability-number">03</div><div class="capability-content"><h4>온·오프라인 리테일</h4><p>더현대, EQL, 롯데월드몰 팝업 처음부터 끝까지 했어요. 검색 유입 <span class="hl-green">150~400% 증가</span>.</p></div></div>
        <div class="capability-item"><div class="capability-number">04</div><div class="capability-content"><h4>AI 기반 업무 자동화</h4><p>SQL로 KPI 대시보드 직접 만들었어요. 회의 자료 만드는 시간 <span class="hl-green">3배 단축</span>.</p></div></div>
    </div></div></section>

    <section class="work"><div class="container"><div class="section-label">WORK</div><h2 class="section-title">Selected Projects</h2><div class="projects-list">

        <article class="project-item">
            <div class="project-header"><div class="project-index">01</div><div class="project-meta"><span class="project-category">셀럽/인플루언서 · IMC · PM</span><span class="project-period">2024.09 - 2025.02</span><span class="project-contribution">기여도: 기획 80% · 실행 100% · 분석 100%</span></div></div>
            <h3 class="project-name">듀베티카 24FW 셀럽/인플루언서 협업 프로젝트</h3>
            <p class="project-summary"><strong>[PM]</strong> 리브랜딩 이후 듀베티카가 가진 <strong>패딩 헤리티지/프리미엄 무드</strong>를 대중에게 확산시키고, <strong>'NEXT 몽클레르'</strong> 포지셔닝을 만들기 위해 셀럽(김지원) → 인플루언서 → 커뮤니티 → 실수요층으로 이어지는 <strong>IMC 메시지 통합</strong>을 설계·실행한 프로젝트입니다.</p>
            <div class="project-strengths"><div class="chips"><span class="chip">IMC 메시지 통합</span><span class="chip">타깃/포지셔닝 재정의</span><span class="chip">셀럽→인플루언서 연결</span><span class="chip">OOH→바이럴 설계</span><span class="chip">데이터 기반 검증</span></div></div>
            <div class="project-media"><div class="media-grid-thumbs"><div class="media-thumb"><img src="{p1_1}" alt="듀베티카 1"></div><div class="media-thumb"><img src="{p1_2}" alt="듀베티카 2"></div><div class="media-thumb"><img src="{p1_3}" alt="듀베티카 3"></div></div></div>
            <div class="project-details-grid">
                <div class="detail-card role"><span class="detail-label">👤 My Role</span><ul><li><strong>기획 (80%)</strong>: 타깃(당당한 3040 도시여성) 재정의, 'NEXT 몽클레르' 포지셔닝 논리 정리</li><li><strong>실행 (100%)</strong>: 셀럽(김지원) 활용 앵글/PR 구체화, 오프라인 이벤트·릴레이 팝업·옥외광고·바이럴까지 연결</li><li><strong>분석 (100%)</strong>: 노출→인스타→커뮤니티→실수요 침투 퍼널로 성과 추적</li></ul></div>
                <div class="detail-card key-insight"><span class="detail-label">💡 Key Insight</span><p class="insight-quote"><strong>"노출은 최대화, 브랜드 가치 납득은 5명만 타겟한다."</strong></p><ul><li>프리미엄 브랜드일수록 '작지만 실수요 커뮤니티'가 납득하면 입소문으로 자연 확산된다</li></ul></div>
                <div class="detail-card result"><span class="detail-label">📈 Result</span><div class="result-metrics"><div class="metric"><span class="metric-value">500만</span><span class="metric-label">셀럽 콘텐츠 조회수</span></div><div class="metric"><span class="metric-value">4배</span><span class="metric-label">키 아이템 매출 증가</span></div><div class="metric"><span class="metric-value">2배</span><span class="metric-label">연간 검색량 & 매출</span></div></div><div class="result-qual"><ul><li><strong>여배우 패딩 이미지</strong> 확립 → "몽클레르 대체템"으로 언급</li></ul></div></div>
            </div>
        </article>

        <article class="project-item">
            <div class="project-header"><div class="project-index">02</div><div class="project-meta"><span class="project-category">Flagship · Collaboration · PM</span><span class="project-period">2025.08 - 2025.10</span><span class="project-contribution">기여도: 기획 100% · 실행 85% · 분석 100%</span></div></div>
            <h3 class="project-name">세르지오 타키니 한남 플래그십 & 콜라보</h3>
            <p class="project-summary"><strong>[PM 총괄]</strong> 한남 플래그십 오픈을 <span class="hl-yellow">로컬 핫플</span>로 만들었어요. 올리베 키링, 현대카드 콜라보까지 직접 기획. 결과는 <span class="hl-green">유입·매출 전환 2배</span>, 오가닉 콘텐츠 <span class="hl-green">400건</span>.</p>
            <div class="project-strengths"><div class="chips"><span class="chip">플래그십 오픈 기획</span><span class="chip">IP 콜라보</span><span class="chip">현장 운영 설계</span><span class="chip">인플루언서 마케팅</span></div></div>
            <div class="project-media"><div class="media-grid-thumbs"><div class="media-thumb"><img src="{p2_1}" alt="한남 플래그십 1"></div><div class="media-thumb"><img src="{p2_2}" alt="한남 플래그십 2"></div><div class="media-thumb"><img src="{p2_3}" alt="한남 플래그십 3"></div></div></div>
            <div class="project-details-grid">
                <div class="detail-card role"><span class="detail-label">👤 My Role</span><ul><li><strong>기획 리드 (100%)</strong>: 플래그십 오픈 행사 기획, 올리베/현대카드 콜라보 기획</li><li><strong>실행 (85%)</strong>: 현장 운영 프로세스 설계, 셀럽/인플루언서 활용 마케팅</li></ul></div>
                <div class="detail-card result"><span class="detail-label">📈 Result</span><div class="result-metrics"><div class="metric"><span class="metric-value">2배</span><span class="metric-label">유입·매출 전환</span></div><div class="metric"><span class="metric-value">300만+</span><span class="metric-label">단일 콘텐츠 조회수</span></div><div class="metric"><span class="metric-value">400건</span><span class="metric-label">오가닉 콘텐츠</span></div></div></div>
            </div>
        </article>

        <article class="project-item">
            <div class="project-header"><div class="project-index">03</div><div class="project-meta"><span class="project-category">Sponsorship · Collaboration · PM</span><span class="project-period">2024.11 - 2024.12</span><span class="project-contribution">기여도: 기획 90% · 실행 80% · 분석 80%</span></div></div>
            <h3 class="project-name">현대카드 슈퍼매치</h3>
            <p class="project-summary"><strong>[PM · Sponsorship Activation]</strong> 테니스 세계 랭킹 1·2위 초청 슈퍼매치 공식 후원을 통해 브랜드 테니스 헤리티지를 각인, <span class="hl-green">2주 내 검색·매출 2배 상승</span>.</p>
            <div class="project-strengths"><div class="chips"><span class="chip">스폰서십 활성화</span><span class="chip">테니스 헤리티지 브랜딩</span><span class="chip">협업 MD 기획</span><span class="chip">오피니언 리더 활용</span></div></div>
            <div class="project-media"><div class="media-grid-thumbs"><div class="media-thumb"><img src="{p3_1}" alt="슈퍼매치 1"></div><div class="media-thumb"><img src="{p3_2}" alt="슈퍼매치 2"></div></div></div>
            <div class="project-details-grid">
                <div class="detail-card role"><span class="detail-label">👤 My Role</span><ul><li><strong>기획 리드 (90%)</strong>: 후원 목표/메시지 정의, 팬덤+대중 공통 앵글 설계</li><li><strong>실행 (80%)</strong>: 오피니언 리더 섭외·콘텐츠 기획, 뉴미디어 채널 운영</li></ul></div>
                <div class="detail-card result"><span class="detail-label">📈 Result</span><div class="result-metrics"><div class="metric"><span class="metric-value">2배</span><span class="metric-label">2주간 검색량·매출</span></div><div class="metric"><span class="metric-value">40만+</span><span class="metric-label">단일 콘텐츠 조회수</span></div><div class="metric"><span class="metric-value">1위</span><span class="metric-label">MD 리오더 주간 판매</span></div></div></div>
            </div>
        </article>

        <article class="project-item">
            <div class="project-header"><div class="project-index">04</div><div class="project-meta"><span class="project-category">Retail Pop-up · PM</span><span class="project-period">2025.02 - 2025.04</span><span class="project-contribution">기여도: 기획 100% · 실행 90% · 분석 100%</span></div></div>
            <h3 class="project-name">세르지오 타키니 EQL 성수 팝업</h3>
            <p class="project-summary"><strong>[PM 리드]</strong> 성수에서 <span class="hl-yellow">'찍고 싶은 공간'</span>을 만들었어요. 제품은 2~3개로 줄이고, 무드에 집중. 결과는 <span class="hl-green">바이럴 300만+</span>, 키 아이템 검색량 <span class="hl-green">2배</span>.</p>
            <div class="project-strengths"><div class="chips"><span class="chip">팝업 공간 기획</span><span class="chip">무드 중심 VMD</span><span class="chip">포토존 설계</span><span class="chip">바이럴 콘텐츠 유도</span></div></div>
            <div class="project-media"><div class="media-grid-thumbs"><div class="media-thumb"><img src="{p4_1}" alt="EQL 팝업 1"></div><div class="media-thumb"><img src="{p4_2}" alt="EQL 팝업 2"></div></div></div>
            <div class="project-details-grid">
                <div class="detail-card role"><span class="detail-label">👤 My Role</span><ul><li><strong>기획 리드 (100%)</strong>: 팝업 비주얼 기획, 브랜드 재해석 전략 수립</li><li><strong>공간 설계</strong>: '고객의 촬영 행동' 중심 공간 구성, 제품 최소화 전략</li></ul></div>
                <div class="detail-card result"><span class="detail-label">📈 Result</span><div class="result-metrics"><div class="metric"><span class="metric-value">300만+</span><span class="metric-label">SNS 바이럴 조회수</span></div><div class="metric"><span class="metric-value">2배</span><span class="metric-label">키 아이템 검색량</span></div></div></div>
            </div>
        </article>

        <article class="project-item">
            <div class="project-header"><div class="project-index">05</div><div class="project-meta"><span class="project-category">Global Event · PM</span><span class="project-period">2025.02 - 2025.05</span><span class="project-contribution">기여도: 기획 100% · 실행 70% · 분석 100%</span></div></div>
            <h3 class="project-name">몬테카를로 마스터즈 MCCC 글로벌 행사</h3>
            <p class="project-summary"><strong>[PM 리드]</strong> 몬테카를로 마스터즈에서 <span class="hl-yellow">오래 쓸 수 있는 콘텐츠</span>를 확보. 셀럽 동선, 착장, 촬영 포인트까지 직접 설계. 결과는 주요 콘텐츠 <span class="hl-green">100~300만 조회</span>.</p>
            <div class="project-strengths"><div class="chips"><span class="chip">글로벌 이벤트 기획</span><span class="chip">셀럽 동선/착장 설계</span><span class="chip">촬영 포인트 기획</span><span class="chip">장기 활용 콘텐츠 확보</span></div></div>
            <div class="project-media"><div class="media-grid-thumbs"><div class="media-thumb"><img src="{p5_1}" alt="MCCC 1"></div><div class="media-thumb"><img src="{p5_2}" alt="MCCC 2"></div><div class="media-thumb"><img src="{p5_3}" alt="MCCC 3"></div></div></div>
            <div class="project-details-grid">
                <div class="detail-card role"><span class="detail-label">👤 My Role</span><ul><li><strong>기획 리드 (100%)</strong>: 셀럽 초청 행사 타임라인 기획, 셀럽 동선·착장·촬영 포인트 설계</li><li><strong>리스크 관리</strong>: 제약조건 속 우선순위 설정, 필수 컷리스트 정의</li></ul></div>
                <div class="detail-card result"><span class="detail-label">📈 Result</span><div class="result-metrics"><div class="metric"><span class="metric-value">3.5만</span><span class="metric-label">메인 콘텐츠 ENG</span></div><div class="metric"><span class="metric-value">100~300만</span><span class="metric-label">주요 콘텐츠 조회수</span></div></div></div>
            </div>
        </article>

        <article class="project-item">
            <div class="project-header"><div class="project-index">06</div><div class="project-meta"><span class="project-category">Strategy · PM</span><span class="project-period">2021.10 - Present</span><span class="project-contribution">기여도: 기획 100% · 실행 60% · 분석 100%</span></div></div>
            <h3 class="project-name">시즌 IMC 전략 수립</h3>
            <p class="project-summary"><strong>[전략 리드]</strong> 매 시즌 <span class="hl-yellow">브랜딩+세일즈 통합 전략</span>을 짜요. KPI 설정, 예산 배분, 부서 조율까지. 결과는 시즌별 <span class="hl-green">인지도·매출 2배+</span> 성장.</p>
            <div class="project-strengths"><div class="chips"><span class="chip">시즌 IMC 전략</span><span class="chip">경쟁사 분석</span><span class="chip">KPI 설정/예산 배분</span><span class="chip">부서 간 조율</span></div></div>
            <div class="project-details-grid">
                <div class="detail-card role"><span class="detail-label">👤 My Role</span><ul><li><strong>전략 리드 (100%)</strong>: 시즌별 상품 전략, KPI, 예산, 플래닝 리드</li><li><strong>데이터 분석 (100%)</strong>: 데이터 기반 전략 및 트렌드 리서치 자료 배포</li><li><strong>템플릿 구축</strong>: 전략/리서치/KPI 운영 자료 템플릿 제작</li></ul></div>
                <div class="detail-card result"><span class="detail-label">📈 Result</span><div class="result-metrics"><div class="metric"><span class="metric-value">2배+</span><span class="metric-label">시즌별 인지도·매출</span></div><div class="metric"><span class="metric-value">템플릿화</span><span class="metric-label">전략/리서치/KPI 자료</span></div><div class="metric"><span class="metric-value">단축</span><span class="metric-label">리드 타임 감소</span></div></div></div>
            </div>
        </article>

        <article class="project-item">
            <div class="project-header"><div class="project-index">07</div><div class="project-meta"><span class="project-category">AI · Automation</span><span class="project-period">2025.08 - Present</span><span class="project-contribution">기여도: 기획 100% · 개발 100% · 분석 100%</span></div></div>
            <h3 class="project-name">AI Agent MKT KPI 대시보드 구축</h3>
            <p class="project-summary"><strong>[개발 리드]</strong> 마케팅 KPI 대시보드를 <span class="hl-yellow">직접 만들었어요</span>. SQL 쿼리 설계부터 자동화까지. 결과는 회의 자료 제작 <span class="hl-green">시간 3배 단축</span>.</p>
            <div class="project-strengths"><div class="chips"><span class="chip">AI 기반 대시보드</span><span class="chip">Snowflake SQL 설계</span><span class="chip">업무 자동화</span><span class="chip">데이터 시각화</span></div></div>
            <div class="project-main-image"><img src="{dashboard}" alt="AI Dashboard"></div>
            <div class="project-details-grid">
                <div class="detail-card role"><span class="detail-label">👤 My Role</span><ul><li><strong>기획 리드 (100%)</strong>: 마케팅 KPI와 판매데이터 연결 구조 설계</li><li><strong>개발 (100%)</strong>: Snowflake SQL 데이터 자동화 쿼리 설계, AI 기반 인사이트 대시보드 제작</li><li><strong>자동화 구축 (100%)</strong>: 주간 회의 자료, CEO 보고 자료 자동화</li></ul></div>
                <div class="detail-card result"><span class="detail-label">📈 Result</span><div class="result-metrics"><div class="metric"><span class="metric-value">3배</span><span class="metric-label">자료 제작 시간 단축</span></div><div class="metric"><span class="metric-value">향상</span><span class="metric-label">의사결정 속도</span></div><div class="metric"><span class="metric-value">감소</span><span class="metric-label">부서 커뮤니케이션</span></div></div></div>
            </div>
        </article>

    </div></div></section>

    <section class="skills"><div class="container"><div class="section-label">SKILLS</div><h2 class="section-title">What I Do</h2><div class="skills-grid">
        <div class="skill-block"><h4>Strategy</h4><ul><li><span class="skill-highlight">IMC 전략 기획</span></li><li>브랜딩·세일즈 퍼널</li><li><span class="skill-highlight">캠페인 스토리텔링</span></li><li><span class="skill-highlight">시즌별 메시지 아키텍처</span></li><li>KPI 설정 및 예산 배분</li></ul></div>
        <div class="skill-block"><h4>Data & Research</h4><ul><li><span class="skill-highlight">경쟁사 분석 및 리서치</span></li><li>시장 트렌드 데이터 분석</li><li>SNS 지표 분석</li><li>CRM 세그먼트 분석</li><li><span class="skill-highlight">데이터 기반 가설 설계</span></li></ul></div>
        <div class="skill-block"><h4>Creative</h4><ul><li><span class="skill-highlight">숏폼 기획</span></li><li><span class="skill-highlight">IP & 브랜드 협업</span></li><li>인플루언서 협업</li><li>촬영 기획/디렉션</li><li><span class="skill-highlight">바이럴 콘텐츠 설계</span></li></ul></div>
        <div class="skill-block"><h4>Tools & Tech</h4><ul><li>Notion · Figma · Excel</li><li>Google Analytics</li><li>Meta / TikTok Business</li><li><span class="skill-highlight">SQL (Snowflake)</span></li><li><span class="skill-highlight">AI 이미지/영상/분석</span></li></ul></div>
    </div></div></section>

    <section class="contact"><div class="container"><div class="contact-wrapper"><div class="contact-content"><div class="section-label">CONTACT</div><h2 class="contact-title">Let's Work<br>Together</h2><p class="contact-description"><strong>뉴미디어 채널과 콘텐츠로 브랜드를 성장시키는 IMC 마케터</strong>입니다.<br>브랜드 커뮤니케이션 전략 수립부터 통합 마케팅, 국내외 협업 캠페인까지<br>채널 × 콘텐츠 × 데이터를 연결해 브랜드를 빌드업합니다.</p><div class="contact-links"><a href="mailto:skswn2@naver.com" class="contact-link"><span class="link-label">Email</span><span class="link-value">skswn2@naver.com</span></a><a href="tel:010-6808-5398" class="contact-link"><span class="link-label">Phone</span><span class="link-value">010-6808-5398</span></a></div></div><div class="contact-profile"><div class="profile-image-wrapper"><img src="{profile}" alt="이난주 프로필"></div></div></div></div></section>

    <footer class="footer"><div class="container"><p>@ 브랜드 마케터 이난주</p></div></footer>
</body>
</html>"""

print("Generating HTML...")
html_content = html_template
for key, value in images.items():
    html_content = html_content.replace("{" + key + "}", value)

with open("이난주_포트폴리오_완전판.html", "w", encoding="utf-8") as f:
    f.write(html_content)

file_size = os.path.getsize("이난주_포트폴리오_완전판.html")
print(f"File created: 이난주_포트폴리오_완전판.html")
print(f"File size: {file_size/1024/1024:.2f} MB")
