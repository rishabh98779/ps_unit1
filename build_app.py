#!/usr/bin/env python3
# Builder for the Probability & Statistics interactive study app.
# Data authored from the raw extracted course source. Assembles one self-contained HTML file.
import json, io, os

HTML_HEAD = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Probability &amp; Statistics — Interactive Study System</title>
<script>
window.MathJax = {
  tex: { inlineMath: [['\\(','\\)'], ['$','$']], displayMath: [['\\[','\\]'], ['$$','$$']] },
  svg: { fontCache: 'global' }
};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
<style>
:root{
  --bg:#0b0f17; --bg2:#111827; --card:#131b2b; --card2:#182236;
  --ink:#e8ecf4; --muted:#94a3b8; --line:#243048;
  --acc:#6d8dfe; --acc2:#22c55e; --warn:#f59e0b; --danger:#f87171;
  --violet:#a78bfa; --cyan:#38bdf8;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:'Segoe UI',system-ui,-apple-system,sans-serif;background:var(--bg);color:var(--ink)}
header{position:sticky;top:0;z-index:50;background:rgba(11,15,23,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--line);display:flex;align-items:center;gap:14px;padding:10px 18px}
header h1{font-size:17px;margin:0;letter-spacing:.4px}
header .brand{display:flex;align-items:center;gap:10px}
.logo{width:34px;height:34px;border-radius:9px;background:linear-gradient(135deg,var(--acc),var(--violet));display:flex;align-items:center;justify-content:center;font-weight:800;color:#fff;font-size:16px}
#search{flex:1;max-width:420px;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:8px 12px;color:var(--ink);font-size:14px}
#search::placeholder{color:var(--muted)}
.layout{display:flex;min-height:calc(100vh - 54px)}
nav{width:264px;flex-shrink:0;border-right:1px solid var(--line);padding:16px 12px;overflow-y:auto;height:calc(100vh - 54px);position:sticky;top:54px}
main{flex:1;padding:26px 34px;max-width:1120px}
nav .navhead{font-size:11px;text-transform:uppercase;letter-spacing:.12em;color:var(--muted);margin:14px 6px 6px}
nav a.u{display:block;color:var(--ink);text-decoration:none;font-weight:650;font-size:14px;padding:7px 8px;border-radius:7px}
nav a.u:hover{background:var(--card)}
nav .t{display:block;color:var(--muted);text-decoration:none;font-size:13px;padding:5px 8px 5px 20px;border-radius:6px;border-left:2px solid transparent}
nav .t:hover{background:var(--card);color:var(--ink)}
nav .t.active{background:var(--card2);color:var(--acc);border-left-color:var(--acc)}
nav .views{margin-bottom:8px}
h2.unit-title{font-size:24px;margin:4px 0 2px;letter-spacing:.2px}
p.unit-sub{color:var(--muted);font-size:14px;margin-top:0}
.topic{margin-bottom:38px}
.badge{display:inline-block;background:var(--card2);color:var(--acc);font-size:11px;font-weight:700;padding:3px 9px;border-radius:20px;letter-spacing:.06em;margin-bottom:8px}
h2.tt{font-size:21px;margin:2px 0 12px;border-bottom:1px solid var(--line);padding-bottom:8px}
.sec{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px 20px;margin:14px 0}
.sec h3{margin:0 0 10px;font-size:15px;color:var(--acc);letter-spacing:.03em}
.sec p{margin:8px 0;line-height:1.65;font-size:14.5px}
.def{border-left:3px solid var(--acc2)}
.def .fd{background:var(--card2);border:1px solid var(--line);border-radius:8px;padding:12px 14px;line-height:1.6;font-size:15px}
.def .kw{margin-top:10px}
.chip{display:inline-block;background:#1e2a3d;color:var(--cyan);font-size:11.5px;padding:3px 8px;border-radius:12px;margin:2px 4px 2px 0;border:1px solid #2b3d55}
.formula-box{background:var(--card2);border:1px solid var(--line);border-radius:8px;padding:12px 16px;margin:8px 0;overflow-x:auto}
.formula-box .note{color:var(--muted);font-size:13px;margin-top:6px}
.ex{border-left:3px solid var(--acc)}
.ex-steps{font-size:14.5px}
.ex-steps .step{background:var(--card2);border:1px solid var(--line);border-radius:8px;padding:10px 14px;margin:8px 0}
.tbl{border-collapse:collapse;width:100%;margin:10px 0;font-size:13.5px}
.tbl th{background:var(--card2);padding:7px 10px;text-align:left;border:1px solid var(--line);color:var(--cyan)}
.tbl td{padding:6px 10px;border:1px solid var(--line)}
details{border:1px solid var(--line);border-radius:8px;background:var(--card2);margin:8px 0}
details>summary{cursor:pointer;padding:9px 14px;font-size:13px;font-weight:600;color:var(--acc);list-style:none}
details>summary::before{content:'▸';margin-right:8px;font-size:11px}
details[open]>summary::before{content:'▾'}
details>summary:hover{color:var(--cyan)}
details .body{padding:4px 16px 12px}
.lvl{font-size:10.5px;font-weight:700;letter-spacing:.05em;padding:2px 8px;border-radius:10px;margin-left:8px;vertical-align:middle}
.l-basic{background:#12351f;color:#4ade80}
.l-standard{background:#13324e;color:#60c5fa}
.l-exam{background:#3a1d4d;color:#d8b4fe}
.l-challenge{background:#4a2505;color:#fdba74}
.src{font-size:10.5px;font-weight:600;padding:2px 8px;border-radius:10px;margin-left:8px;vertical-align:middle;background:#25324a;color:#9db4d8}
.warnbox{background:#2a1d07;border:1px solid #6b4d12;color:#fcd34d;padding:10px 14px;border-radius:8px;font-size:13px;margin:10px 0}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px}
.dash-card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px}
.dash-card h3{margin:0 0 8px;font-size:15px;color:var(--acc)}
.stat{font-size:28px;font-weight:800;color:var(--ink)}
.progress{height:8px;background:var(--card2);border-radius:6px;overflow:hidden;margin:8px 0}
.progress>div{height:100%;background:linear-gradient(90deg,var(--acc),var(--acc2));width:0%}
.fb{margin-bottom:26px}
.fb h4{margin:0 0 6px;font-size:14px;color:var(--acc2)}
.qcard{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:12px 0}
.qcard .q{font-size:14.5px;line-height:1.6;margin:6px 0}
.filters{display:flex;flex-wrap:wrap;gap:10px;margin:14px 0}
.filters select,.filters input{background:var(--card);border:1px solid var(--line);color:var(--ink);border-radius:8px;padding:7px 10px;font-size:13px}
.btn{background:var(--card2);border:1px solid var(--line);color:var(--acc);border-radius:7px;padding:5px 12px;font-size:12px;cursor:pointer;font-weight:600}
.btn:hover{border-color:var(--acc)}
.stat-chips{display:flex;flex-wrap:wrap;gap:12px;margin:12px 0}
.stat-chips .chip2{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 14px;font-size:13px}
.hero{background:linear-gradient(135deg,#1a2340,#10182c);border:1px solid var(--line);border-radius:16px;padding:30px 32px;margin-bottom:22px}
.hero h2{font-size:26px;margin:0 0 8px}
.hero p{color:var(--muted);max-width:760px;line-height:1.6}
.toc-chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px}
.toc-chips a{background:var(--card2);border:1px solid var(--line);color:var(--ink);text-decoration:none;font-size:12px;padding:6px 12px;border-radius:20px}
.toc-chips a:hover{border-color:var(--acc);color:var(--acc)}
mark{background:#5b4a00;color:#fff}
.small{color:var(--muted);font-size:12.5px}
.co-table{border-collapse:collapse;width:100%;font-size:13px}
.co-table th,.co-table td{border:1px solid var(--line);padding:8px 10px;text-align:left}
.co-table th{background:var(--card2);color:var(--cyan)}
@media (max-width:860px){nav{display:none}main{padding:18px}}
</style>
</head>
<body>
<header>
  <div class="brand"><div class="logo">P&amp;S</div><h1>Probability &amp; Statistics — Interactive Study System</h1></div>
  <input id="search" placeholder="Search topics, definitions, formulas, questions…" oninput="doSearch(this.value)">
</header>
<div class="layout">
<nav id="nav"></nav>
<main id="main"></main>
</div>
"""

FRAMEWORK_JS = r"""
// ============ RENDER FRAMEWORK ============
function mathTex(s){return s}
function esc(s){return s}
function renderSection(s){
  let h='';
  if(s.type==='def'){
    h+='<div class="sec def">';
    if(s.title)h+='<h3>'+s.title+'</h3>';
    if(s.formal)h+='<div class="fd"><b>Formal Definition (Exam-Ready):</b><br>'+s.formal+'</div>';
    if(s.hinglish)h+='<p><b>Hinglish Explanation:</b> '+s.hinglish+'</p>';
    if(s.keywords){h+='<div class="kw"><b>Keywords to Remember:</b> ';s.keywords.forEach(k=>h+='<span class="chip">'+k+'</span>');h+='</div>'}
    h+='</div>';
  } else if(s.type==='text'){
    h+='<div class="sec">';
    if(s.title)h+='<h3>'+s.title+'</h3>';
    h+='<p>'+s.body+'</p></div>';
  } else if(s.type==='list'){
    h+='<div class="sec">';
    if(s.title)h+='<h3>'+s.title+'</h3><ul>';
    s.items.forEach(i=>h+='<li style="margin:5px 0;font-size:14.5px;line-height:1.55">'+i+'</li>');
    h+='</ul></div>';
  } else if(s.type==='formula'){
    h+='<div class="sec">';
    if(s.title)h+='<h3>'+s.title+'</h3>';
    s.items.forEach(f=>{
      h+='<div class="formula-box">'+f.latex;
      if(f.vars)h+='<div class="note"><b>Notation:</b> '+f.vars+'</div>';
      if(f.note)h+='<div class="note">'+f.note+'</div>';
      h+='</div>';
    });
    h+='</div>';
  } else if(s.type==='example'){
    h+='<div class="sec ex">';
    h+='<h3>'+s.title+'</h3>';
    h+='<p><b>Problem:</b> '+s.problem+'</p>';
    if(s.asked)h+='<p><b>What is being asked?</b> '+s.asked+'</p>';
    if(s.given)h+='<p><b>Given:</b> '+s.given+'</p>';
    if(s.method)h+='<p><b>Method:</b> '+s.method+'</p>';
    if(s.formula)h+='<div class="formula-box">'+s.formula+'</div>';
    if(s.steps){h+='<div class="ex-steps">';s.steps.forEach((st,i)=>{h+='<div class="step"><b>Step '+(i+1)+':</b> '+st+'</div>'});h+='</div>'}
    if(s.answer)h+='<p style="background:#12351f;border:1px solid #1e5c36;padding:9px 12px;border-radius:8px"><b>Final Answer:</b> '+s.answer+'</p>';
    if(s.tip)h+='<p><b>Exam Tip:</b> '+s.tip+'</p>';
    h+='</div>';
  } else if(s.type==='try'){
    h+='<div class="sec"><h3>Try Yourself';
    h+='</h3><p class="q">'+s.problem+'</p>';
    if(s.hint)h+='<details><summary>Show Hint</summary><div class="body"><p>'+s.hint+'</p></div></details>';
    if(s.answer)h+='<details><summary>Reveal Answer</summary><div class="body"><p><b>Answer:</b> '+s.answer+'</p></div></details>';
    if(s.solution){h+='<details><summary>Show Full Solution</summary><div class="body">';s.solution.forEach(st=>h+='<p>'+st+'</p>');h+='</div></details>'}
    h+='</div>';
  } else if(s.type==='derive'){
    h+='<div class="sec"><h3>'+s.title+'</h3>';
    s.steps.forEach(st=>h+='<p>'+st+'</p>');
    h+='</div>';
  }
  return h;
}
function lvlTag(l){const m={Basic:'l-basic',Standard:'l-standard',Exam:'l-exam',Challenge:'l-challenge'};return '<span class="lvl '+m[l]+'">'+l+'</span>'}
function renderTopic(t){
  let h='<div class="topic" id="'+t.id+'">';
  h+='<span class="badge">'+t.code+'</span><h2 class="tt">'+t.title+'<span class="small" id="mark-'+t.id+'" style="margin-left:10px;cursor:pointer;color:var(--muted)" onclick="toggleDone(\''+t.id+'\')">○ unmarked</span></h2>';
  t.sections.forEach(s=>h+=renderSection(s));
  h+='</div>';
  return h;
}
let COURSE=(typeof COURSE_DATA!=='undefined'?COURSE_DATA:{units:[]});
let QB=(typeof QB_DATA!=='undefined'?QB_DATA:[]);
function buildNav(){
  let h='<div class="views"><div class="navhead">Views</div>';
  h+='<a class="u" href="#home" onclick="showHome()">Dashboard</a>';
  h+='<a class="u" href="#defbank" onclick="showDefBank()">Definition Bank</a>';
  h+='<a class="u" href="#formulas" onclick="showFormulas()">Formula Sheet</a>';
  h+='<a class="u" href="#qbank" onclick="showQBank()">Master Question Bank</a></div>';
  COURSE.units.forEach(u=>{
    h+='<div class="navhead">'+u.title+'</div>';
    u.topics.forEach(t=>{h+='<a class="t" id="nav-'+t.id+'" href="#'+t.id+'" onclick="goTopic(\''+t.id+'\')">'+t.title+'</a>'});
  });
  document.getElementById('nav').innerHTML=h;
}
function renderUnit(u,showT){
  let h='<h2 class="unit-title">'+u.title+'</h2><p class="unit-sub">'+u.sub+'</p>';
  u.topics.forEach(t=>{ if(!showT||t.id===showT){h+=renderTopic(t)} else if(showT){h+='<div style="display:none">'+renderTopic(t)+'</div>'} });
  return h;
}
function goTopic(id){
  let html='';let found=false;
  COURSE.units.forEach(u=>u.topics.forEach(t=>{if(t.id===id){html=renderUnit(u,id);found=true}}));
  if(found){
    document.getElementById('main').innerHTML=html;
    document.querySelectorAll('nav .t').forEach(a=>a.classList.remove('active'));
    let n=document.getElementById('nav-'+id);if(n)n.classList.add('active');
    renderMath();window.scrollTo(0,0);
  }
}
function renderMath(){if(window.MathJax&&MathJax.typesetPromise){MathJax.typesetPromise();}}
let DONES=JSON.parse(localStorage.getItem('psdones')||'[]');
function toggleDone(id){
  let i=DONES.indexOf(id);
  if(i>=0)DONES.splice(i,1);else DONES.push(id);
  localStorage.setItem('psdones',JSON.stringify(DONES));
  refreshDoneMarks();
}
function refreshDoneMarks(){
  DONES.forEach(id=>{let el=document.getElementById('mark-'+id);if(el){el.textContent='✔ completed';el.style.color='var(--acc2)'}});
}
function showHome(){
  let total=0,done=DONES.length;
  COURSE.units.forEach(u=>total+=u.topics.length);
  let qn=0;QB.forEach(q=>qn++);
  let defs=0;COURSE.units.forEach(u=>u.topics.forEach(t=>t.sections.forEach(s=>{if(s.type==='def')defs++})));
  let h='<div class="hero"><h2>Probability &amp; Statistics — Digital Textbook + Exam System</h2>'
   +'<p>Yeh app aapke official course material par based hai — Units, topics aur examples seedha uploaded source se organized kiye gaye hain. Har topic mein formal exam-ready definition, Hinglish explanation, formulas, solved examples, try-yourself practice aur exam focus milega. Neeche se unit choose karo ya sidebar se kahin bhi jump karo.</p>'
   +'<div class="toc-chips">';
  COURSE.units.forEach(u=>h+='<a href="#" onclick="openUnit(\''+u.id+'\');return false">'+u.title+'</a>');
  h+='</div></div>';
  h+='<div class="grid2">'
   +'<div class="dash-card"><h3>Study Progress</h3><div class="progress"><div style="width:'+(100*done/Math.max(total,1))+'%"></div></div><p class="small">'+done+' of '+total+' topics marked complete. Topics ko mark karne ke liye topic heading ke paas "unmarked" par click karo.</p></div>'
   +'<div class="dash-card"><h3>Exam Arsenal</h3><div class="stat-chips"><div class="chip2"><b>'+defs+'</b> formal definitions</div><div class="chip2"><b>'+qn+'</b> question-bank items</div><div class="chip2"><b>'+COURSE.units.length+'</b> syllabus units</div></div><p class="small">Definition Bank, Formula Sheet aur Question Bank sidebar se available hain.</p></div>'
   +'</div>';
  h+='<div class="sec"><h3>Course Outcomes (from official course material)</h3><table class="co-table"><tr><th>CO</th><th>BT Level</th><th>Description</th></tr>';
  CO_TABLE.forEach(r=>h+='<tr><td>'+r[0]+'</td><td>'+r[1]+'</td><td>'+r[2]+'</td></tr>');
  h+='</table><p class="small">Learning Outcomes (source): (1) role of statistics in engineering data analysis, (2) classify measures of central tendency and dispersion, (3) significance of skewness and kurtosis in distribution shapes.</p></div>';
  h+='<div class="sec"><h3>How to use this system</h3><ul>'
   +'<li><b>Learn:</b> Topic-wise sections follow Definition → Hinglish Explanation → Formula → Method → Solved Examples → Try Yourself → Common Mistakes → Exam Focus.</li>'
   +'<li><b>Memorize:</b> Definition Bank is rapid pre-exam revision — definition, Hinglish meaning and keywords ek jagah.</li>'
   +'<li><b>Revise formulas:</b> Formula Sheet groups every formula by the official syllabus structure with notation meaning.</li>'
   +'<li><b>Practice:</b> Master Question Bank mein filters hain — unit, topic, difficulty, type aur solved/unsolved ke hisaab se drill karo.</li></ul></div>';
  document.getElementById('main').innerHTML=h;renderMath();window.scrollTo(0,0);
}
function openUnit(uid){
  let u=COURSE.units.find(x=>x.id===uid);
  document.getElementById('main').innerHTML=renderUnit(u,null);renderMath();window.scrollTo(0,0);refreshDoneMarks();
}
function showDefBank(){
  let h='<h2 class="unit-title">Definition Bank</h2><p class="unit-sub">Rapid pre-exam memorization: formal definition → Hinglish meaning → keywords.</p>';
  COURSE.units.forEach(u=>{
    h+='<h2 class="unit-title" style="font-size:18px">'+u.title+'</h2>';
    u.topics.forEach(t=>t.sections.forEach(s=>{
      if(s.type==='def'){
        h+='<div class="fb"><h4>'+t.title+(s.title&&s.title!=='Formal Definition'?' — '+s.title:'')+'</h4>';
        if(s.formal)h+='<div class="fd">'+s.formal+'</div>';
        if(s.hinglish)h+='<p><b>Hinglish:</b> '+s.hinglish+'</p>';
        if(s.keywords){h+='<div class="kw">';s.keywords.forEach(k=>h+='<span class="chip">'+k+'</span>');h+='</div>'}
        h+='</div>';
      }
    }));
  });
  document.getElementById('main').innerHTML=h;renderMath();window.scrollTo(0,0);
}
function showFormulas(){
  let h='<h2 class="unit-title">Master Formula Sheet</h2><p class="unit-sub">Formulas organized exactly by the official syllabus structure. Har formula ke saath notation aur applicable data type diya gaya hai.</p>';
  COURSE.units.forEach(u=>{
    h+='<h2 class="unit-title" style="font-size:17px">'+u.title+'</h2>';
    u.topics.forEach(t=>t.sections.forEach(s=>{
      if(s.type==='formula'){
        h+='<div class="sec"><h3>'+t.title+(s.title?' — '+s.title.replace(/^Formulas?/,"").trim():'')+'</h3>';
        s.items.forEach(f=>{
          h+='<div class="formula-box">'+f.latex;
          if(f.vars)h+='<div class="note">'+f.vars+'</div>';
          if(f.note)h+='<div class="note">'+f.note+'</div>';
          h+='</div>';
        });
        h+='</div>';
      }
    }));
  });
  document.getElementById('main').innerHTML=h;renderMath();window.scrollTo(0,0);
}
QB = QB||[];
function showQBank(){
  let units=[...new Set(QB.map(q=>q.unit))], topics=[...new Set(QB.map(q=>q.topic))], diffs=[...new Set(QB.map(q=>q.diff))], types=[...new Set(QB.map(q=>q.type))];
  let h='<h2 class="unit-title">Master Question Bank</h2><p class="unit-sub">Comprehensive exam practice repository. Hint, answer aur solution hidden hain — pehle khud solve karo.</p>';
  h+='<div class="filters"><select id="fu" onchange="filterQB()"><option value="">All Units</option>'+units.map(x=>`<option>${x}</option>`).join('')+'</select>'
   +'<select id="ft" onchange="filterQB()"><option value="">All Topics</option>'+topics.map(x=>`<option>${x}</option>`).join('')+'</select>'
   +'<select id="fd" onchange="filterQB()"><option value="">All Difficulties</option>'+diffs.map(x=>`<option>${x}</option>`).join('')+'</select>'
   +'<select id="fy" onchange="filterQB()"><option value="">All Types</option>'+types.map(x=>`<option>${x}</option>`).join('')+'</select>'
   +'<select id="fs" onchange="filterQB()"><option value="">Solved + Unsolved</option><option value="solved">Solved only</option><option value="unsolved">Answer not in source</option></select></div>';
  h+='<div id="qb-list"></div>';
  document.getElementById('main').innerHTML=h;filterQB();window.scrollTo(0,0);
}
function filterQB(){
  const fu=document.getElementById('fu').value, ft=document.getElementById('ft').value, fd=document.getElementById('fd').value, fy=document.getElementById('fy').value, fs=document.getElementById('fs').value;
  let list=QB.filter(q=>(!fu||q.unit===fu)&&(!ft||q.topic===ft)&&(!fd||q.diff===fd)&&(!fy||q.type===fy)&&(!fs||(fs==='solved'?q.answerAvailable:fs==='unsolved'?!q.answerAvailable:true)));
  let h='<p class="small">'+list.length+' questions match.</p>';
  list.forEach((q,i)=>{
    h+='<div class="qcard"><span class="lvl '+(q.diff==='Basic'?'l-basic':q.diff==='Standard'?'l-standard':q.diff==='Exam'?'l-exam':'l-challenge')+'">'+q.diff+'</span><span class="src">'+q.type+'</span><span class="src">'+q.unit+' · '+q.topic+'</span>';
    h+='<p class="q"><b>Q'+(i+1)+'.</b> '+q.q+'</p>';
    if(q.hint)h+='<details><summary>Show Hint</summary><div class="body"><p>'+q.hint+'</p></div></details>';
    if(q.answer){h+='<details><summary>Reveal Answer</summary><div class="body"><p><b>Answer:</b> '+q.answer+'</p>';h+='<p class="small">Source status: '+(q.answerAvailable?'Answer extracted from source material.':'Generated solution — source question ke liye yeh solution independently derive kiya gaya hai hai.')+'</p></div></details>'}
    else{h+='<p class="small">Answer not provided in source.</p>'}
    if(q.solution){h+='<details><summary>Show Full Solution</summary><div class="body">';q.solution.forEach(st=>h+='<p>'+st+'</p>');h+='</div></details>'}
    h+='</div>';
  });
  document.getElementById('qb-list').innerHTML=h;renderMath();
}
function doSearch(q){
  if(!q||q.length<3){if(location.hash&&location.hash!=='#home')return;showHome();return}
  let res=[];
  COURSE.units.forEach(u=>u.topics.forEach(t=>{
    let blob=t.title+' '+t.sections.map(s=>[s.title||'',s.formal||'',s.hinglish||'',s.body||'',(s.items?s.items.map(i=>i.replace?i:(i.latex||'')+(i.vars||'')+(i.note||'')):[]).join(' ')].join(' ')).join(' ');
    if(blob.toLowerCase().includes(q.toLowerCase()))res.push({t:t,u:u});
  }));
  QB.forEach(qq=>{if(qq.q.toLowerCase().includes(q.toLowerCase()))res.push({q:qq})});
  let h='<h2 class="unit-title">Search results</h2><p class="small">'+res.length+' results for "'+q+'"</p>';
  res.forEach(r=>{
    if(r.t)h+='<div class="qcard"><p class="q"><b>Topic:</b> '+r.t.title+' <span class="small">('+r.u.title+')</span></p><button class="btn" onclick="goTopic(\''+r.t.id+'\')">Open topic</button></div>';
    else h+='<div class="qcard"><p class="q"><b>Question:</b> '+r.q.q+'</p></div>';
  });
  document.getElementById('main').innerHTML=h;renderMath();
}
window.addEventListener('error',e=>{ let d=document.getElementById('dbg')||(()=>{let x=document.createElement('div');x.id='dbg';x.style.cssText='position:fixed;bottom:4px;right:4px;background:#700;color:#fff;font-size:11px;padding:2px 8px;z-index:99';document.body.appendChild(x);return x})(); d.textContent='JS error: '+(e.message||'unknown'); });
window.addEventListener('load',()=>{
  buildNav();
  const h=location.hash;
  if(h==='#defbank')showDefBank();
  else if(h==='#formulas')showFormulas();
  else if(h==='#qbank')showQBank();
  else if(h&&h!=='#home')goTopic(h.slice(1));
  else showHome();
  refreshDoneMarks();
});
"""

# ================= ASSEMBLY =================
import json, importlib
from course_data import DATA, CO_TABLE
import data_u1_rest, data_u2, data_u3, data_u4, qb_data

# attach rest of unit1 topics
u1 = DATA["units"][0]
u1["topics"].extend(data_u1_rest.u1_rest)
DATA["units"].extend([data_u2.u2, data_u3.u3, data_u4.u4])

course_json = json.dumps(DATA, ensure_ascii=False)
co_json = json.dumps(CO_TABLE, ensure_ascii=False)
qb_json = json.dumps(qb_data.QB, ensure_ascii=False)

html = HTML_HEAD
html += "<script>const COURSE_DATA = " + course_json + ";\n"
html += "const CO_TABLE = " + co_json + ";\n"
html += "const QB_DATA = " + qb_json + ";</script>\n"
html += "<script>" + FRAMEWORK_JS + "</script>\n"
html += "</body></html>"



out = "/workspace/project/probability_statistics_study_app.html"
with open(out, "w", encoding="utf-8") as f:
    f.write(html)
print("Wrote", out, len(html), "bytes")
