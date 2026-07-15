"use client";

import { FormEvent, useState } from "react";

type View = "prototype" | "workflow" | "decisions";

const productSystems = [
  ["01", "Fuel systems", "Carburetors, jets, manifolds and tuning components"],
  ["02", "Intake systems", "Air filters and intake solutions"],
  ["03", "Engine systems", "Performance and maintenance components"],
  ["04", "Control systems", "Handlebars, grips, levers and rider controls"],
  ["05", "Braking systems", "Components built for confident control"],
  ["06", "Electronic systems", "Ignition and electrical performance parts"],
  ["07", "Transmission systems", "Drivetrain and power-delivery components"],
  ["08", "Rider gear", "Off-road jerseys, suits, gloves and goggles"],
];

const workflow = [
  { n: "01", phase: "目标与资料盘点", input: "业务目标、目标市场、现有数据与素材", codex: "资料归档、缺口清单、项目简报", human: "确认优先市场与商业目标", output: "经批准的项目 Brief" },
  { n: "02", phase: "竞品与用户研究", input: "竞品名单、搜索数据、销售反馈", codex: "竞品页面拆解、用户意图、机会点", human: "补充一线市场判断", output: "参考库与策略假设" },
  { n: "03", phase: "信息架构", input: "品牌优势、政策、线索标准", codex: "页面结构、用户路径、表单分层", human: "确认必须展示/保密内容", output: "页面框架 V1" },
  { n: "04", phase: "文案与证据", input: "事实、证书、案例、服务能力", codex: "中英文文案、CTA、FAQ、证据映射", human: "核实事实并审批承诺", output: "可发布文案包" },
  { n: "05", phase: "UI 原型", input: "视觉规范、图片、页面框架", codex: "桌面/移动原型、交互状态", human: "评审品牌感与业务逻辑", output: "可点击原型 V1/V2" },
  { n: "06", phase: "开发与集成", input: "技术栈、CRM/邮箱、隐私条款", codex: "前端页面、表单校验、埋点方案", human: "提供账户权限与路由规则", output: "测试环境页面" },
  { n: "07", phase: "QA 与上线", input: "测试清单、审批意见", codex: "多端检查、SEO/性能/表单测试", human: "法务和商业最终签字", output: "上线版本与验收单" },
  { n: "08", phase: "监测与优化", input: "访问、点击、表单、销售结果", codex: "周/月报、漏斗诊断、A/B 假设", human: "回传线索质量与成交信息", output: "迭代 Backlog" },
];

const references = [
  { type: "行业", name: "Parts Europe", lesson: "在申请前清楚列出门店、资质和经营要求，减少低质量线索。", url: "https://www.partseurope.eu/sign-up/" },
  { type: "行业", name: "Royal Enfield", lesson: "先解释筛选流程与合作关系，再进入申请，增强可信度。", url: "https://www.royalenfield.com/in/en/forms/become-a-dealer/" },
  { type: "行业", name: "Highway Hawk", lesson: "用价格、物流、产品范围和支持直接回答经销商最关心的问题。", url: "https://www.highwayhawk.com/request-dealer-access/" },
  { type: "跨行业", name: "Herman Miller", lesson: "强调长期伙伴价值、培训、营销支持与成长路径。", url: "https://www.hermanmiller.com/en_afr/contact/become-a-herman-miller-dealer/" },
  { type: "跨行业", name: "Patagonia", lesson: "以品牌契合度、经营能力和完整资料做深度资格筛选。", url: "https://dealer.patagonia.com/apply/" },
];

function ReviewTag({ children = "待确认" }: { children?: string }) {
  return <span className="review-tag">{children}</span>;
}

export default function Home() {
  const [view, setView] = useState<View>("prototype");
  const [review, setReview] = useState(false);
  const [sent, setSent] = useState(false);

  function submit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setSent(true);
  }

  return (
    <main className={review ? "review-on" : ""}>
      <div className="reviewbar">
        <div><strong>NIBBI Dealer Page · V1 Discussion Prototype</strong><span>Internal review · 15 Jul 2026</span></div>
        <nav className="view-switch" aria-label="Prototype views">
          <button className={view === "prototype" ? "active" : ""} onClick={() => setView("prototype")}>页面原型</button>
          <button className={view === "workflow" ? "active" : ""} onClick={() => setView("workflow")}>协作工作流</button>
          <button className={view === "decisions" ? "active" : ""} onClick={() => setView("decisions")}>待决策清单</button>
        </nav>
        <label className="toggle"><input type="checkbox" checked={review} onChange={e => setReview(e.target.checked)} /><span />评审标注</label>
      </div>

      {view === "prototype" && (
        <>
          <header className="site-header">
            <a className="brand" href="#top"><b>NIBBI</b><span>RACING</span></a>
            <nav><a href="#why">Why NIBBI</a><a href="#systems">Product Systems</a><a href="#support">Dealer Support</a><a href="#process">How It Works</a></nav>
            <a className="button small" href="#apply">Apply now <span>↗</span></a>
          </header>

          <section className="hero" id="top">
            <img src="./nibbi/hero.webp" alt="NIBBI Racing off-road riders" />
            <div className="hero-shade" />
            <div className="hero-content">
              <p className="eyebrow">BECOME A NIBBI DEALER</p>
              <h1>Bring performance<br />to your market.</h1>
              <p className="hero-copy">Build your next growth line with a carburetor-led, off-road performance ecosystem designed around riders, workshops and real-world tuning.</p>
              <div className="actions"><a className="button" href="#apply">Start your application <span>↗</span></a><a className="text-link" href="#why">Explore the partnership ↓</a></div>
            </div>
            <div className="hero-index"><span>01</span><i /><span>08</span></div>
          </section>

          <section className="signal-strip">
            <div><b>8</b><span>Product systems</span></div>
            <div><b>2026</b><span>Current product catalog</span></div>
            <div><b>R&D</b><span>Race-informed development</span></div>
            <div><b>B2B</b><span>Built for long-term partners</span></div>
          </section>

          <section className="why section" id="why">
            <div className="section-kicker">01 / WHY PARTNER WITH NIBBI</div>
            <div className="why-grid">
              <div className="big-statement"><h2>More than parts.<br /><em>A performance system.</em></h2><p>NIBBI connects fuel delivery, intake, control, braking, electronics, transmission and rider gear into one focused off-road product story.</p></div>
              <div className="image-stack"><img src="./nibbi/rally.jpg" alt="NIBBI rally motorcycle" /><span className="caption">BUILT AROUND THE RIDE</span></div>
            </div>
            <div className="benefit-grid">
              <article><span>01</span><h3>Category depth</h3><p>A broad product system gives dealers more cross-sell paths than a single hero SKU.</p></article>
              <article><span>02</span><h3>Technical story</h3><p>Fitment, tuning and product knowledge create value at the counter and in the workshop.</p></article>
              <article><span>03</span><h3>Content engine</h3><p>Product, racing, factory and rider assets can support local launches and education.</p></article>
              <article><span>04</span><h3>Growth partnership</h3><p>Qualification, onboarding and ongoing review align both sides for sustainable growth.</p><ReviewTag>支持细则待定</ReviewTag></article>
            </div>
          </section>

          <section className="systems section dark" id="systems">
            <div className="section-kicker yellow">02 / PRODUCT ECOSYSTEM</div>
            <div className="systems-head"><h2>One brand.<br />Eight ways to grow.</h2><p>Start with the categories that fit your market, then expand the basket as product knowledge and demand grow.</p></div>
            <div className="system-list">{productSystems.map(([n, title, copy]) => <article key={n}><span>{n}</span><h3>{title}</h3><p>{copy}</p><b>↗</b></article>)}</div>
          </section>

          <section className="support section" id="support">
            <div className="support-visual"><img src="./nibbi/paddock.webp" alt="NIBBI paddock technical support" /><div><span>TRACK</span><span>WORKSHOP</span><span>MARKET</span></div></div>
            <div className="support-copy"><div className="section-kicker">03 / DEALER ENABLEMENT</div><h2>Support that moves from launch to sell-through.</h2>
              <ul>
                <li><b>01</b><span><strong>Product onboarding</strong>Category, fitment and product knowledge materials.</span></li>
                <li><b>02</b><span><strong>Marketing toolkit</strong>Approved brand, product and campaign assets for local use.</span><ReviewTag>物料范围待定</ReviewTag></li>
                <li><b>03</b><span><strong>Technical support</strong>A structured path for installation and tuning questions.</span><ReviewTag>SLA待定</ReviewTag></li>
                <li><b>04</b><span><strong>Commercial growth</strong>Regular performance review and market planning.</span><ReviewTag>机制待定</ReviewTag></li>
              </ul>
            </div>
          </section>

          <section className="process section" id="process">
            <div className="section-kicker">04 / HOW IT WORKS</div><h2>A clear path from interest<br />to market launch.</h2>
            <div className="process-line">{[
              ["01", "Apply", "Tell us about your business and market."],
              ["02", "Qualify", "We review channel fit, capability and territory."],
              ["03", "Align", "Discuss range, commercial terms and expectations."],
              ["04", "Onboard", "Complete account setup and product training."],
              ["05", "Grow", "Launch, review performance and expand together."],
            ].map(([n,t,c]) => <article key={n}><b>{n}</b><i /><h3>{t}</h3><p>{c}</p></article>)}</div>
            <p className="process-note"><ReviewTag>建议承诺审核时效前，先确认内部线索SLA</ReviewTag></p>
          </section>

          <section className="fit section dark">
            <div><div className="section-kicker yellow">05 / PARTNER PROFILE</div><h2>Built for dealers who know the ride—and the market.</h2></div>
            <div className="fit-list"><p><span>01</span>Established motorcycle, powersports or performance-parts business</p><p><span>02</span>Strong knowledge of local riders, channels and product demand</p><p><span>03</span>Ability to provide credible sales and customer support</p><p><span>04</span>Commitment to building the NIBBI brand for the long term</p><ReviewTag>准入标准待销售确认</ReviewTag></div>
          </section>

          <section className="proof section">
            <div className="proof-image"><img src="./nibbi/factory.webp" alt="NIBBI production and quality control" /></div>
            <div><div className="section-kicker">06 / PROOF, NOT PROMISES</div><h2>Show the system behind the product.</h2><p>The final page should connect factory capability, quality control, R&D, racing validation and dealer outcomes to verifiable evidence.</p><div className="proof-placeholder"><b>DEALER SUCCESS STORY</b><span>Reserved for a named dealer, market, challenge, action and measurable result.</span><ReviewTag>案例证据待补</ReviewTag></div></div>
          </section>

          <section className="apply section" id="apply">
            <div className="apply-intro"><div className="section-kicker yellow">07 / START THE CONVERSATION</div><h2>Ready to build your market with NIBBI?</h2><p>This V1 uses progressive qualification: the first form is short enough to complete, while the sales team collects legal and financial documents only after initial fit is confirmed.</p><div className="form-note"><b>What happens next</b><span>Application review → Sales contact → Qualification call → Commercial discussion</span><ReviewTag>时效待确认</ReviewTag></div></div>
            <form onSubmit={submit}>
              <div className="fields"><label>Full name<input required placeholder="Your name" /></label><label>Business email<input required type="email" placeholder="name@company.com" /></label><label>Company name<input required placeholder="Company" /></label><label>Country / market<input required placeholder="Country or region" /></label><label>Primary sales channel<select required defaultValue=""><option value="" disabled>Select one</option><option>Physical retail store</option><option>Workshop / service center</option><option>Distributor / wholesaler</option><option>Online retail</option><option>Multi-channel</option></select></label><label>Years in business<select required defaultValue=""><option value="" disabled>Select one</option><option>Less than 1 year</option><option>1–3 years</option><option>4–10 years</option><option>10+ years</option></select></label></div>
              <label>Tell us about your business<textarea required placeholder="Current brands, customer base, sales coverage and why NIBBI fits your market" /></label>
              <label className="consent"><input type="checkbox" required /> I agree that NIBBI may use this information to evaluate and contact me about a potential dealer relationship.</label>
              <button className="button submit" type="submit">{sent ? "Prototype received ✓" : "Submit application ↗"}</button>
              {sent && <p className="success">Demo only — no information was transmitted.</p>}
            </form>
          </section>

          <section className="faq section"><div><div className="section-kicker">08 / FAQ</div><h2>Before you apply.</h2></div><div className="faq-list"><details open><summary>What types of businesses can apply?<span>＋</span></summary><p>Proposed scope: established motorcycle retailers, workshops, performance-parts specialists, distributors and qualified multi-channel sellers.</p></details><details><summary>Is there a minimum opening order?<span>＋</span></summary><p>Commercial terms should be shared after qualification and may vary by market, product range and partner type.</p><ReviewTag>MOQ待销售确认</ReviewTag></details><details><summary>Is territory exclusivity available?<span>＋</span></summary><p>Regional authorization should depend on market potential, coverage plan and agreed performance milestones.</p><ReviewTag>授权规则待定</ReviewTag></details><details><summary>What warranty and technical support is included?<span>＋</span></summary><p>The public answer should link to an approved warranty policy and a clear dealer support path before launch.</p><ReviewTag>政策待补</ReviewTag></details></div></section>

          <footer><a className="brand light" href="#top"><b>NIBBI</b><span>RACING</span></a><p>Performance parts. Serious partnership.</p><a href="#apply">BECOME A DEALER ↗</a><small>V1 discussion prototype · Not for public release</small></footer>
        </>
      )}

      {view === "workflow" && (
        <section className="internal-page">
          <div className="internal-hero"><p className="eyebrow">NIBBI × CODEX OPERATING MODEL</p><h1>从资料到上线，<br />让每一步都有输入、负责人和交付物。</h1><p>建议由业务负责人掌握商业判断与最终审批，Codex承担高频的信息整理、研究、结构、内容、原型、开发与质量检查。</p></div>
          <div className="workflow-table"><div className="workflow-row workflow-head"><span>阶段</span><span>输入</span><span>可交付给 Codex</span><span>团队必须负责</span><span>输出</span></div>{workflow.map(x => <div className="workflow-row" key={x.n}><span><b>{x.n}</b>{x.phase}</span><span>{x.input}</span><span>{x.codex}</span><span>{x.human}</span><span>{x.output}</span></div>)}</div>
          <div className="handoff-grid"><article className="lead"><span>CODEX LEAD</span><h2>可以完整交付</h2><p>资料整理与摘要、竞品研究、信息架构、线框/网页原型、中英文文案初稿、SEO框架、表单设计、埋点方案、QA清单、数据周报/月报与迭代建议。</p></article><article><span>CO-PILOT</span><h2>需要共同完成</h2><p>品牌定位、价值主张、准入标准、经销权益、线索评分、地区策略、案例包装。Codex负责结构与草案，业务团队提供事实并决策。</p></article><article className="human"><span>HUMAN SIGN-OFF</span><h2>不能替代审批</h2><p>折扣与MOQ、独家授权、保修承诺、法务条款、证书/业绩真实性、预算、CRM权限、最终上线和对外发布。</p></article></div>
          <section className="cadence"><div><span>建议节奏</span><h2>一个页面项目的最小闭环</h2></div><ol><li><b>每周一</b>团队补充资料与决策</li><li><b>周二–周三</b>Codex交付研究/内容/原型迭代</li><li><b>周四</b>业务、销售、品牌集中评审</li><li><b>周五</b>形成批准版本与下周Backlog</li></ol></section>
        </section>
      )}

      {view === "decisions" && (
        <section className="internal-page decisions-page">
          <div className="internal-hero"><p className="eyebrow">V1 LEADERSHIP REVIEW</p><h1>这次会议只需要<br />拍板 7 件事。</h1><p>其余内容可以在方向确认后由团队与 Codex 继续细化，不必在第一轮陷入逐字修改。</p></div>
          <div className="decision-list">{[
            ["01", "页面核心目标", "优先获取高质量经销商线索，还是优先建立品牌与渠道信任？建议：以线索为主、信任为转化前提。"],
            ["02", "目标伙伴范围", "零售店、维修店、区域分销商、电商卖家分别是否接受？是否按市场采用不同准入条件？"],
            ["03", "公开到什么程度", "折扣、MOQ、区域授权、保修、物流哪些公开，哪些仅在资格审核后由销售说明？"],
            ["04", "NIBBI核心卖点", "产品系统深度、技术能力、供应链、赛车验证、营销支持中，前三个排序是什么？"],
            ["05", "证据优先级", "先补经销商案例、工厂/质检证据、证书、赛事结果，还是服务SLA？建议：先案例与服务流程。"],
            ["06", "表单与跟进", "第一步只收6项核心信息，还是一次收齐资质文件？谁接收线索、几天内响应、如何判定有效？"],
            ["07", "品牌历史口径", "现有材料出现1983与1985两个起始年份，正式上线前必须统一并确认来源。"],
          ].map(([n,t,c]) => <article key={n}><b>{n}</b><h2>{t}</h2><p>{c}</p><span>OWNER: LEADERSHIP / SALES / BRAND</span></article>)}</div>
          <section className="reference-section"><div><p className="eyebrow">REFERENCE LOGIC</p><h2>参考的是决策逻辑，不是照搬视觉。</h2></div><div>{references.map(r => <a key={r.name} href={r.url} target="_blank" rel="noreferrer"><span>{r.type}</span><h3>{r.name} ↗</h3><p>{r.lesson}</p></a>)}</div></section>
          <section className="source-status"><h2>现有资料状态</h2><div><p><b>可直接用于V1</b>2026产品目录、产品系统分类、品牌/工厂/赛事图片、申请字段框架。</p><p><b>整理后可用</b>公司简介中的品牌历史、工厂、研发、质量与赛事内容；需逐条确认口径。</p><p><b>上线前必补</b>经销权益、折扣/MOQ、授权规则、保修、物流、技术支持SLA、真实经销商案例、隐私条款与线索路由。</p></div></section>
        </section>
      )}
    </main>
  );
}
