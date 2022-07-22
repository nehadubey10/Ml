<!DOCTYPE html>
<!-- saved from url=(0099)https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/texts/21184868-iris-model-ipynb -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<link href="https://cdn.thinkific.com/" rel="preconnect">
<link crossorigin="true" href="https://fonts.gstatic.com/" rel="preconnect">
<link rel="preload" href="./iris_files/vendor-4d6e9185450966c0cabdb0b6ab7efd2c.js.download" as="script" crossorigin="">
<link rel="preload" href="./iris_files/course-player-v2-c9365a5eaafcb1fceba95a2e1d99f0e4.js.download" as="script" crossorigin="">
<link rel="preload" href="./iris_files/vendor-e0cb822bbe090c173fe20baeb13b0c48.css" as="style" crossorigin="">
<link rel="preload" href="./iris_files/course-player-v2-1d5f5c8f7cd184ceb6a823cfd93940aa.css" as="style" crossorigin="">




<script async="" src="./iris_files/analytics.js.download"></script><script>
  window.Thinkific = window.Thinkific || {};
  window.Thinkific.current_user = {"id":40777349,"first_name":"Neha","last_name":"Dubey","email":"nehadubet@gmail.com","external_source":null,"subdomain":"lms1stopai","full_name":"Neha Dubey","created_at":1614761063,"last_sign_in_at":1615996538,"number_courses_complete":0,"external_id":null,"tenant_id":425312,"groups":[{"name":"Machine Learning _E Learning  \u0026 Project_Beat The Virus","token":"6f2e89e6"}]};
</script>

<title>Support's School</title>


<!--[if lt IE 9]>
<script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script>
<![endif]-->
<meta http-equiv="X-UA-Compatible" content="IE=edge">

<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">

<link href="./iris_files/css" rel="stylesheet" type="text/css">
<link rel="shortcut icon" type="image/x-icon" href="https://cdn.thinkific.com/51/20180809/f1a1de9d3260c96d3a81ee781bc9808e.ico">
<meta name="csrf-param" content="authenticity_token">
<meta name="csrf-token" content="Z2D0gapP1Iuf1I67JTX2lJeQSlnvt8yfAmIDrIaUPgQe450r8ksmWA++KZjDtr5rnaEKMib0sCt7tROv3hBWXw==">



<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
  
  var thinkific_google_analytics_disabled = ""
  if (!thinkific_google_analytics_disabled) {
    var tcd = "thinkific.com";
    ga('create', 'UA-30557184-1', 'auto', { 'cookieDomain': tcd });
    ga('send', 'pageview');
  }
  
  var tenantGoogleAnalyticsKey = "";
  
  if(tenantGoogleAnalyticsKey) {
    var tenantCD = "lms1stopai.thinkific.com";
    ga('create', tenantGoogleAnalyticsKey, 'auto', { 'name': 'tenantTracker', 'cookieDomain': tenantCD });
    ga('tenantTracker.send', 'pageview');
  }
</script>



<link href="./iris_files/toga-icons.css" rel="stylesheet" type="text/css">
<link href="./iris_files/toga-product-icons.css" rel="stylesheet" type="text/css">
<meta name="kobayashi" content="553c0529551eacd8d20a0ca4a3e191d69b58e62a">
<link rel="stylesheet" media="all" href="./iris_files/froala-v2-custom-theme-ce387945bbe5675a3124139056696f51721f6c75bc13a83788dad8e2826ab00e.css">
<link rel="stylesheet" href="./iris_files/vendor-e0cb822bbe090c173fe20baeb13b0c48.css">
<link rel="stylesheet" href="./iris_files/course-player-v2-1d5f5c8f7cd184ceb6a823cfd93940aa.css">
<meta name="description" content="Machine Learning _E Learning  &amp; Project_Beat The Virus - Support&#39;s School">
<style>
  
</style>
<link rel="stylesheet" href="./iris_files/main.css"></head>
<body id="courses" class="take lms1stopai-tenant  course-id-1180077"><noscript>
<style>
  body {
    height: 100vh;
    max-width: 100vw;
    margin: 0;
  }
  #wrap {
    display: none;
  }
  .noscript-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    padding: 10px;
    text-align: center;
    background-color: #eee;
  }
  .noscript-container i {
    font-size: 50px;
  }
  .noscript-container h3 {
    margin-bottom: 10px;
    font-weight: 700;
    font-size: 24px;
    line-height: 1.2;
  }
  .noscript-container p {
    font-size: 16px;
    color: #929292;
  }
  .noscript-container a {
    color: #1b9eea;
  }
  .noscript-container a.btn,
  .noscript-container a.btn:visited {
    padding: 8px 20px;
    margin-top: 20px;
    border: 1px solid #929292;
    border-radius: 3px;
    font-weight: 700;
    text-decoration: none;
    color: inherit;
  }
  .noscript-container a.btn:hover {
    background-color: #e6e6e6;
  }
</style>
<div class='noscript-container'>
<i class='icon-settings'></i>
<h3>The content is here but you need to enable JavaScript to view it.</h3>
<p>Please <a rel= "noreferrer noopener" target="_blank" href="https://www.enable-javascript.com">enable JavaScript</a> in your browser settings and reload the page.</p>
<a class="btn" href="">Reload page</a>
</div>
</noscript>

<div id="wrap">
<div id="data-store">
<input id="CourseSlug" type="hidden" value="ml-e-learning-content">
</div>
<div id="page-content" class="ember-application"><div id="modal-overlays"></div><div id="ember399" class="ember-view"><!----><a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/texts/21184868-iris-model-ipynb#main-content" class="skip-link">
  Missing translation: course_player_skip_to_main_content
</a>
<div class="course-player  _course-player_1jimy1">
<!---->    <link href="./iris_files/css(1)" rel="stylesheet">

<style>
  body,
  button,
  input,
  textarea {
    font-family:Source Sans Pro;
  }
  [data-theme] .brand-color__background {
    background-color:#e6aa67;
  }

  [data-theme] .brand-color__text {
    color:#e6aa67;
  }

  [data-theme] .brand-color__dynamic-text {
    color:#1d1d1d;
  }

  [data-theme] .brand-color__fill {
    fill:#e6aa67;
  }

  [data-theme] .brand-color__border {
    border-color:#e6aa67;
  }

  [data-theme] .brand-color__border-60-opacity {
    border-color:rgba(230, 170, 103, 0.6);
  }

  [data-theme] .brand-color__border-60-opacity:not([disabled]):hover {
    border-color:#e6aa67;
  }

  [data-theme] .brand-color__background-30-opacity:not([disabled]):hover {
    background-color:rgba(230, 170, 103, 0.3);
  }

  .course-player__content-item .toga-icon-checkmark::before {
    color:#1d1d1d !important;
  }

  .course-player__chapter-item__header .toga-icon-checkmark::before {
    color:#1d1d1d !important;
  }
</style>

  <div data-theme="light-theme" id="player-wrapper" class="course-player__container  _course-player__container_n1vbpj">
    <!---->
      <header class="course-player__top-bar brand-color__background  _top-bar_n1vbpj">
        <div class="_container_v3q4ce">
  <button aria-label="Enable menu" class="course-player__top-bar__menu-toggle brand-color__dynamic-text _top-bar__menu-toggle_v3q4ce" data-ember-action="" data-ember-action-652="652">
    <span class="course-player__top-bar__menu-toggle__bar _top-bar__menu-toggle__bar_v3q4ce"></span>
    <span class="course-player__top-bar__menu-toggle__bar _top-bar__menu-toggle__bar_v3q4ce"></span>
    <span class="course-player__top-bar__menu-toggle__bar _top-bar__menu-toggle__bar_v3q4ce"></span>
  </button>

  <div class="top-bar__dashboard-link _top-bar__dashboard-link_v3q4ce">
      <a href="https://lms1stopai.thinkific.com/enrollments" class="top-bar__dashboard-link__anchor brand-color__dynamic-text">
        <i aria-hidden="true" class="top-bar__dashboard-link__icon toga-icon toga-icon-caret-stroke-left brand-color__dynamic-text"></i>
        Go to Dashboard
      </a>
  </div>
  <section class="course-player__top-bar__branding _top-bar__branding_v3q4ce">
      <h1 class="course-player__top-bar__site-name brand-color__dynamic-text _top-bar__site-name_v3q4ce"><span>Support's School</span></h1>
  </section>
</div>

      </header>
      <div class="course-player__content     _course-player__content_n1vbpj">

        <nav class="course-player__left-drawer _left-drawer_n1vbpj">
          <div class="course-player__course-navigation _course-navigation_t2nzf7">

  <div id="ember667" class="ember-view"><section class="course-progress__container _course-progress__container_1rtg53">
<section class="surface__container _surface__container_1yatsw _surface--default_1yatsw">
      <div class="course-progress__school-name brand-color__background _course-progress__school-name_1rtg53">
      <div class="_container_v3q4ce">
  <button aria-label="Enable menu" class="course-player__top-bar__menu-toggle brand-color__dynamic-text _top-bar__menu-toggle_v3q4ce" data-ember-action="" data-ember-action-676="676">
    <span class="course-player__top-bar__menu-toggle__bar _top-bar__menu-toggle__bar_v3q4ce"></span>
    <span class="course-player__top-bar__menu-toggle__bar _top-bar__menu-toggle__bar_v3q4ce"></span>
    <span class="course-player__top-bar__menu-toggle__bar _top-bar__menu-toggle__bar_v3q4ce"></span>
  </button>

  <div class="top-bar__dashboard-link _top-bar__dashboard-link_v3q4ce">
      <a href="https://lms1stopai.thinkific.com/enrollments" class="top-bar__dashboard-link__anchor brand-color__dynamic-text">
        <i aria-hidden="true" class="top-bar__dashboard-link__icon toga-icon toga-icon-caret-stroke-left brand-color__dynamic-text"></i>
        Go to Dashboard
      </a>
  </div>
  <section class="course-player__top-bar__branding _top-bar__branding_v3q4ce">
      <h1 class="course-player__top-bar__site-name brand-color__dynamic-text _top-bar__site-name_v3q4ce"><span>Support's School</span></h1>
  </section>
</div>

    </div>
    <div class="course-progress__inner-container _course-progress__inner-container_1rtg53">
      <a href="https://lms1stopai.thinkific.com/enrollments" class="course-progress__dashboard-link _course-progress__dashboard-link_1rtg53">Go to Dashboard</a>
      <h2 class="course-progress__title _course-progress__title_1rtg53">Machine Learning _E Learning  &amp; Project_Beat The Virus</h2>
      <div class="_course-progress__actions-container_1rtg53">
        <div class="_course-progress__progress-bar__container_1rtg53">
          <div style="width:98%;" class="brand-color__background _course-progress__progress-bar__inner_1rtg53"></div>
        </div>
        <p class="course-progress__percent-complete _course-progress__percent-complete_1rtg53"><span>98%</span> complete</p>
<!---->      </div>
    </div>

</section>
</section>
</div>

  <div id="ember697" class=" ember-view"><div class="course-player__user-search _container_56qan">
<div id="ember719" class="ember-basic-dropdown ember-view">
<div aria-owns="ember-basic-dropdown-content-ember719" tabindex="0" data-ebd-id="ember719-trigger" role="button" id="ember724" class="ember-power-select-trigger ember-basic-dropdown-trigger ember-basic-dropdown-trigger--in-place ember-view">    <span class="ember-power-select-placeholder">Search by lesson title</span>

<span class="ember-power-select-status-icon"></span>
</div>
  <div id="ember-basic-dropdown-content-ember719" style="display: none;" class="ember-basic-dropdown-content-placeholder"></div>

</div>
  <div id="user-content-search-power-select" class="course-player__user-search--power-select"></div>
</div>
</div>

  <div role="navigation" aria-label="Chapters" class="course-player__chapters-menu ">
    <ul id="ember752" class="course-player__chapters-item _chapters-item_1tqvoe ember-view ui-accordion ui-widget ui-helper-reset" role="tablist"><div class="course-player__chapter-item__header _chapter-item__header_d57kmg ui-accordion-header ui-corner-top ui-state-default ui-accordion-icons ui-accordion-header-collapsed ui-corner-all" role="tab" id="ui-id-1" aria-controls="ui-id-2" aria-selected="false" aria-expanded="false" tabindex="0"><span class="ui-accordion-header-icon ui-icon ui-icon-triangle-1-e"></span>
  <div class="course-player__chapter-item__container _chapter-item__container_d57kmg">
    <span class="course-player__progress _chapter-item__progress_d57kmg">
      <span data-percentage-completion="100" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="100" class="_chapter-item__progress-ring_d57kmg">
        <span class="progress-ring__ring _progress-ring__ring_jgsecr">
	<span class="progress-ring__mask progress-ring--full _progress-ring__mask_jgsecr _progress-ring--full_jgsecr">
		<span class="progress-ring--fill brand-color__background _progress-ring--fill_jgsecr"></span>
	</span>
	<span class="progress-ring__mask progress-ring--half _progress-ring__mask_jgsecr ">
		<span class="progress-ring--fill brand-color__background _progress-ring--fill_jgsecr"></span>
		<span class="progress-ring--fill progress-ring--fix _progress-ring--fill_jgsecr _progress-ring--fix_jgsecr"></span>
	</span>
</span>
<span class="progress-ring__ring-inset _progress-ring__ring-inset_jgsecr"></span>
<span class="progress-ring__checkmark brand-color__text _progress-ring__checkmark_jgsecr"><i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark"></i></span>

      </span>
    </span>

    <h3 class="_chapter-item__title_d57kmg">ML_E-Learning Content</h3>

<!---->
      <span class="sr-only">Completed</span>

    <span aria-hidden="true" class="course-player__chapter-item__completion _chapter-item__completion_d57kmg">
      51 / 51
    </span>

    <span class="course-player__chapter-item__toggle _chapter-item__toggle_d57kmg">
      <i aria-hidden="true" class="chapter-item__toggle-icon toga-icon toga-icon-caret-stroke-down _chapter-item__toggle-icon_d57kmg"></i>
    </span>
  </div>
</div>
<div class="ui-accordion-content ui-corner-bottom ui-helper-reset ui-widget-content" id="ui-id-2" aria-labelledby="ui-id-1" role="tabpanel" aria-hidden="true" style="display: none;">
  <ul class="course-player__chapter-item__contents _chapter-item__contents_d57kmg">
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-772="772">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/22264751-chapter-1-introduction-to-python" id="ember777" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Chapter 1 - Introduction to Python
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 1 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-791="791">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21186925-anaconda-installation" id="ember792" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Anaconda installation
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 1 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-799="799">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21186930-jupyter-notebooks" id="ember800" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Jupyter notebooks
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 3 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-807="807">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21186960-chapter-2-why-python-features-of-python" id="ember808" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Chapter 2 - Why Python - Features of Python
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 1 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-815="815">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21186973-multi-paradigm" id="ember816" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Multi Paradigm
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 1 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-823="823">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21186979-open-source" id="ember824" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Open source
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· &lt; 1 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-831="831">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21186981-diversified" id="ember832" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Diversified
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 1 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-839="839">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187193-interpretation" id="ember840" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Interpretation
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 1 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-847="847">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187199-easy-and-simple" id="ember848" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Easy and simple
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· &lt; 1 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-855="855">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187251-dynamic-typing" id="ember856" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Dynamic typing
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 2 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-863="863">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187207-large-standard-library" id="ember864" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Large Standard library
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 1 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-871="871">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187265-chapter-3-numbers-and-variables-numbers" id="ember872" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Chapter 3 - Numbers and Variables - Numbers
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 4 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-879="879">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187272-operators" id="ember880" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Operators
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 2 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-887="887">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187278-variables" id="ember888" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Variables
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 4 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-895="895">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187280-dynamic-typing" id="ember896" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Dynamic Typing
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 1 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-903="903">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187306-chapter-4-strings" id="ember904" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Chapter 4 - Strings
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 5 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-911="911">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187389-string-methods" id="ember912" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      String Methods
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 3 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-919="919">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187401-string-operations" id="ember920" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      String Operations
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 6 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-927="927">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187409-immutability" id="ember928" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Immutability
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 3 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-935="935">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187415-string-formatting" id="ember936" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      String Formatting
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 6 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-943="943">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187486-chapter-5-lists" id="ember944" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Chapter 5 - Lists
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 5 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-951="951">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187530-list-methods" id="ember952" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      List_Methods
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 5 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-959="959">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187539-tuples" id="ember960" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Tuples
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 4 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-967="967">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187542-dictionaries" id="ember968" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Dictionaries
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 4 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-975="975">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187544-dic-methods" id="ember976" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Dic_Methods
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 3 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-983="983">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187548-sets-and-booleans" id="ember984" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Sets and Booleans
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 4 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-991="991">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187603-chapter-6-statements" id="ember992" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Chapter 6 - Statements
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 5 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-999="999">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187606-for-loop" id="ember1000" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      For loop
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 3 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1007="1007">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187610-while-loops" id="ember1008" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      While loops
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 4 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1015="1015">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187624-chapter-7-functions" id="ember1016" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Chapter 7 - Functions
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 4 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1023="1023">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187629-decorators" id="ember1024" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Decorators
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 2 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1031="1031">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187636-generators" id="ember1032" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Generators
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 3 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1039="1039">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187643-chapter-8-object-oriented-programming-oop-objects-and-classes" id="ember1040" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Chapter 8 - Object Oriented Programming (OOP) - Objects and Classes
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 5 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1047="1047">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187665-attributes" id="ember1048" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Attributes
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 5 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1055="1055">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187674-methods" id="ember1056" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Methods
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 11 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1063="1063">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187676-inheritance" id="ember1064" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Inheritance
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 7 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1071="1071">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187694-polymorphism" id="ember1072" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Polymorphism
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 6 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1079="1079">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21159106-supervised-learning" id="ember1080" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Supervised Learning
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 6 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1087="1087">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21159114-supervised-learning-pdf" id="ember1088" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Supervised Learning PDF
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1102="1102">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21159123-unsupervised-machine-learning" id="ember1103" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Unsupervised Machine Learning
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 7 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1110="1110">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21159130-unsupervised-machine-learning-pdf" id="ember1111" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Unsupervised Machine Learning PDF
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1118="1118">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21159157-reinforcement-machine-learning" id="ember1119" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Reinforcement Machine Learning
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 4 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1126="1126">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21159162-reinforcement-machine-learning-pdf" id="ember1127" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Reinforcement Machine Learning PDF
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1134="1134">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21159207-classification" id="ember1135" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Classification
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 6 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1142="1142">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21159213-classification-pdf" id="ember1143" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Classification PDF
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1150="1150">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21163609-regression" id="ember1151" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Regression
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 6 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1158="1158">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21163628-regression-pdf" id="ember1159" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Regression.PDF
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1166="1166">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21163648-clustering" id="ember1167" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Clustering
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 5 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1174="1174">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21163667-clustering-pdf" id="ember1175" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Clustering.pdf
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1182="1182">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21163703-association" id="ember1183" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Association
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 5 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1190="1190">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21163719-association-pdf" id="ember1191" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Association.PDF
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
  </ul>
</div>
</ul>
    <ul id="ember1197" class="course-player__chapters-item _chapters-item_1tqvoe ember-view ui-accordion ui-widget ui-helper-reset" role="tablist"><div class="course-player__chapter-item__header _chapter-item__header_d57kmg ui-accordion-header ui-corner-top ui-accordion-header-collapsed ui-corner-all ui-state-default ui-accordion-icons" role="tab" id="ui-id-3" aria-controls="ui-id-4" aria-selected="false" aria-expanded="false" tabindex="0"><span class="ui-accordion-header-icon ui-icon ui-icon-triangle-1-e"></span>
  <div class="course-player__chapter-item__container _chapter-item__container_d57kmg">
    <span class="course-player__progress _chapter-item__progress_d57kmg">
      <span data-percentage-completion="100" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="100" class="_chapter-item__progress-ring_d57kmg">
        <span class="progress-ring__ring _progress-ring__ring_jgsecr">
	<span class="progress-ring__mask progress-ring--full _progress-ring__mask_jgsecr _progress-ring--full_jgsecr">
		<span class="progress-ring--fill brand-color__background _progress-ring--fill_jgsecr"></span>
	</span>
	<span class="progress-ring__mask progress-ring--half _progress-ring__mask_jgsecr ">
		<span class="progress-ring--fill brand-color__background _progress-ring--fill_jgsecr"></span>
		<span class="progress-ring--fill progress-ring--fix _progress-ring--fill_jgsecr _progress-ring--fix_jgsecr"></span>
	</span>
</span>
<span class="progress-ring__ring-inset _progress-ring__ring-inset_jgsecr"></span>
<span class="progress-ring__checkmark brand-color__text _progress-ring__checkmark_jgsecr"><i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark"></i></span>

      </span>
    </span>

    <h3 class="_chapter-item__title_d57kmg">ML - Gmail Spam Detection from Beat The Virus_Project - 1</h3>

<!---->
      <span class="sr-only">Completed</span>

    <span aria-hidden="true" class="course-player__chapter-item__completion _chapter-item__completion_d57kmg">
      18 / 18
    </span>

    <span class="course-player__chapter-item__toggle _chapter-item__toggle_d57kmg">
      <i aria-hidden="true" class="chapter-item__toggle-icon toga-icon toga-icon-caret-stroke-down _chapter-item__toggle-icon_d57kmg"></i>
    </span>
  </div>
</div>
<div class="ui-accordion-content ui-corner-bottom ui-helper-reset ui-widget-content" id="ui-id-4" aria-labelledby="ui-id-3" role="tabpanel" aria-hidden="true" style="display: none;">
  <ul class="course-player__chapter-item__contents _chapter-item__contents_d57kmg">
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1209="1209">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187796-supervised-learning" id="ember1210" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Supervised Learning
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 6 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1217="1217">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21187871-supervised-learning-pdf" id="ember1218" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Supervised Learning PDF
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1225="1225">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21187888-unsupervised-machine-learning" id="ember1226" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Unsupervised Machine Learning
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 7 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1233="1233">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21190445-unsupervised-machine-learning-pdf" id="ember1234" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Unsupervised Machine Learning PDF
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1241="1241">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21190460-reinforcement-machine-learning" id="ember1242" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Reinforcement Machine Learning
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 4 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1249="1249">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21190468-reinforcement-machine-learning-pdf" id="ember1250" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Reinforcement Machine Learning PDF
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1257="1257">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21190607-classification" id="ember1258" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Classification
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 6 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1265="1265">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21190610-classification-pdf" id="ember1266" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Classification PDF
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1273="1273">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21190616-regression" id="ember1274" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Regression
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 6 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1281="1281">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21190621-regression-pdf" id="ember1282" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Regression PDF
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1289="1289">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21192293-clustering" id="ember1290" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Clustering
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 5 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1297="1297">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21192299-clustering-pdf" id="ember1298" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Clustering PDF
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1305="1305">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21190661-association" id="ember1306" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Association
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 5 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1313="1313">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21190664-association-pdf" id="ember1314" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Association PDF
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1321="1321">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21183870-gmail-spam-detection" id="ember1322" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Gmail Spam Detection 
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 12 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1329="1329">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/texts/21183967-gmail-spam-detection-code" id="ember1330" class="course-player__content-item__link _content-item__link_nffvg8 ember-transitioning-in ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Gmail Spam Detection -code
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-text _content-item__type-icon_nffvg8"></i>
          Text
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1344="1344">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/texts/21183977-spam-csv" id="ember1345" class="course-player__content-item__link _content-item__link_nffvg8 ember-transitioning-in ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Spam.csv
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-text _content-item__type-icon_nffvg8"></i>
          Text
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1352="1352">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21183986-gmail-spam-detection" id="ember1353" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Gmail_spam detection
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
  </ul>
</div>
</ul>
    <ul id="ember1359" class="course-player__chapters-item _chapters-item_1tqvoe ember-view ui-accordion ui-widget ui-helper-reset" role="tablist"><div class="course-player__chapter-item__header _chapter-item__header_d57kmg ui-accordion-header ui-corner-top ui-state-default ui-accordion-icons ui-accordion-header-collapsed ui-corner-all" role="tab" id="ui-id-5" aria-controls="ui-id-6" aria-selected="false" aria-expanded="false" tabindex="0"><span class="ui-accordion-header-icon ui-icon ui-icon-triangle-1-e"></span>
  <div class="course-player__chapter-item__container _chapter-item__container_d57kmg">
    <span class="course-player__progress _chapter-item__progress_d57kmg">
      <span data-percentage-completion="100" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="100" class="_chapter-item__progress-ring_d57kmg">
        <span class="progress-ring__ring _progress-ring__ring_jgsecr">
	<span class="progress-ring__mask progress-ring--full _progress-ring__mask_jgsecr _progress-ring--full_jgsecr">
		<span class="progress-ring--fill brand-color__background _progress-ring--fill_jgsecr"></span>
	</span>
	<span class="progress-ring__mask progress-ring--half _progress-ring__mask_jgsecr ">
		<span class="progress-ring--fill brand-color__background _progress-ring--fill_jgsecr"></span>
		<span class="progress-ring--fill progress-ring--fix _progress-ring--fill_jgsecr _progress-ring--fix_jgsecr"></span>
	</span>
</span>
<span class="progress-ring__ring-inset _progress-ring__ring-inset_jgsecr"></span>
<span class="progress-ring__checkmark brand-color__text _progress-ring__checkmark_jgsecr"><i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark"></i></span>

      </span>
    </span>

    <h3 class="_chapter-item__title_d57kmg">ML - Diabetes Detection from Beat The Virus_Project - 2</h3>

<!---->
      <span class="sr-only">Completed</span>

    <span aria-hidden="true" class="course-player__chapter-item__completion _chapter-item__completion_d57kmg">
      18 / 18
    </span>

    <span class="course-player__chapter-item__toggle _chapter-item__toggle_d57kmg">
      <i aria-hidden="true" class="chapter-item__toggle-icon toga-icon toga-icon-caret-stroke-down _chapter-item__toggle-icon_d57kmg"></i>
    </span>
  </div>
</div>
<div class="ui-accordion-content ui-corner-bottom ui-helper-reset ui-widget-content" id="ui-id-6" aria-labelledby="ui-id-5" role="tabpanel" aria-hidden="true" style="display: none;">
  <ul class="course-player__chapter-item__contents _chapter-item__contents_d57kmg">
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1371="1371">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21192034-supervised-learning" id="ember1372" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Supervised Learning
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 6 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1379="1379">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21192037-supervised-learning-pdf" id="ember1380" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Supervised Learning PDF
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1387="1387">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21192042-unsupervised-machine-learning" id="ember1388" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Unsupervised Machine Learning
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 7 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1395="1395">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21192047-unsupervised-machine-learning-pdf" id="ember1396" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Unsupervised Machine Learning PDF
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1403="1403">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21192058-reinforcement-machine-learning" id="ember1404" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Reinforcement Machine Learning
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 4 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1411="1411">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21192062-reinforcement-machine-learning-pdf" id="ember1412" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Reinforcement Machine Learning PDF
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1419="1419">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21192085-classification" id="ember1420" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Classification
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 6 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1427="1427">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21192132-classification-pdf" id="ember1428" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Classification PDF
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1435="1435">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21192135-regression" id="ember1436" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Regression
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 6 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1443="1443">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21192141-regression-pdf" id="ember1444" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Regression PDF
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1451="1451">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21192148-clustering" id="ember1452" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Clustering
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 5 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1459="1459">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21192161-clustering-pdf" id="ember1460" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Clustering PDF
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1467="1467">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21192202-association" id="ember1468" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Association
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 5 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1475="1475">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21192205-association-pdf" id="ember1476" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Association.PDF
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1483="1483">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21184482-dibetes-detection" id="ember1484" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Dibetes Detection 
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 10 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1491="1491">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21184787-diabetes-predication-ppt" id="ember1492" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Diabetes predication.ppt
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1499="1499">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/texts/21184795-diabetes-csv" id="ember1500" class="course-player__content-item__link _content-item__link_nffvg8 ember-transitioning-in ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Diabetes .csv
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-text _content-item__type-icon_nffvg8"></i>
          Text
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1507="1507">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/texts/21184804-diabetes-code" id="ember1508" class="course-player__content-item__link _content-item__link_nffvg8 ember-transitioning-in ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Diabetes.code
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-text _content-item__type-icon_nffvg8"></i>
          Text
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
  </ul>
</div>
</ul>
    <ul id="ember1514" class="course-player__chapters-item _chapters-item_1tqvoe ember-view ui-accordion ui-widget ui-helper-reset" role="tablist"><div class="course-player__chapter-item__header _chapter-item__header_d57kmg ui-accordion-header ui-corner-top ui-state-default ui-accordion-icons ui-accordion-header-active ui-state-active" role="tab" id="ui-id-7" aria-controls="ui-id-8" aria-selected="true" aria-expanded="true" tabindex="0"><span class="ui-accordion-header-icon ui-icon ui-icon-triangle-1-s"></span>
  <div class="course-player__chapter-item__container _chapter-item__container_d57kmg">
    <span class="course-player__progress _chapter-item__progress_d57kmg">
      <span data-percentage-completion="80" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="80" class="_chapter-item__progress-ring_d57kmg">
        <span class="progress-ring__ring _progress-ring__ring_jgsecr">
	<span class="progress-ring__mask progress-ring--full _progress-ring__mask_jgsecr _progress-ring--full_jgsecr">
		<span class="progress-ring--fill brand-color__background _progress-ring--fill_jgsecr"></span>
	</span>
	<span class="progress-ring__mask progress-ring--half _progress-ring__mask_jgsecr ">
		<span class="progress-ring--fill brand-color__background _progress-ring--fill_jgsecr"></span>
		<span class="progress-ring--fill progress-ring--fix _progress-ring--fill_jgsecr _progress-ring--fix_jgsecr"></span>
	</span>
</span>
<span class="progress-ring__ring-inset _progress-ring__ring-inset_jgsecr"></span>
<span class="progress-ring__checkmark brand-color__text _progress-ring__checkmark_jgsecr"><i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark"></i></span>

      </span>
    </span>

    <h3 class="_chapter-item__title_d57kmg">ML - IRIS Classification_Project - 3</h3>

<!---->
<!---->
    <span aria-hidden="true" class="course-player__chapter-item__completion _chapter-item__completion_d57kmg">
      4 / 5
    </span>

    <span class="course-player__chapter-item__toggle _chapter-item__toggle_d57kmg">
      <i aria-hidden="true" class="chapter-item__toggle-icon toga-icon toga-icon-caret-stroke-down _chapter-item__toggle-icon_d57kmg"></i>
    </span>
  </div>
</div>
<div class="ui-accordion-content ui-corner-bottom ui-helper-reset ui-widget-content ui-accordion-content-active" id="ui-id-8" aria-labelledby="ui-id-7" role="tabpanel" aria-hidden="false" style="">
  <ul class="course-player__chapter-item__contents _chapter-item__contents_d57kmg">
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1522="1522">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21192382-supervised-learning" id="ember1523" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Supervised Learning
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 6 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1530="1530">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/pdfs/21192389-supervised-learning-pdf" id="ember1531" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      Supervised Learning PDF
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-pdf _content-item__type-icon_nffvg8"></i>
          PDF
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1538="1538">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/lessons/21184862-iris-classification" id="ember1539" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      IRIS Classification
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-video _content-item__type-icon_nffvg8"></i>
          Video
            <span class="content-item__metadata text-capitalize">&nbsp;· 8 min</span>
<!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--complete _content-item_nffvg8" data-ember-action="" data-ember-action-1546="1546">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/texts/21184868-iris-model-ipynb" id="ember1547" class="course-player__content-item__link _content-item__link_nffvg8 active ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i role="img" aria-label="Completed" class="toga-icon toga-icon-checkmark course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      IRIS -MODEL.IPYNB
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-text _content-item__type-icon_nffvg8"></i>
          Text
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
      <li class="course-player__content-item released content-item__progress--viewed _content-item_nffvg8" data-ember-action="" data-ember-action-1554="1554">
<a href="https://lms1stopai.thinkific.com/courses/take/ml-e-learning-content/assignments/21184889-iris-csv-csv" id="ember1555" class="course-player__content-item__link _content-item__link_nffvg8 ember-view">    <div class="brand-color__text _content-item__progress_nffvg8">
        <i aria-hidden="true" class="content-item__progress-icon content-item__progress-icon--circle course-player__content-item__progress-icon _content-item__progress-icon_nffvg8"></i>
    </div>
    <div class="content-item__title _content-item__title_nffvg8">
      IRIS.CSV.CSV
      <div class="content-item__details _content-item__details_nffvg8">
            <i aria-hidden="true" class="toga-icon toga-icon-content-assignment _content-item__type-icon_nffvg8"></i>
          Assignment
<!----><!----><!----><!---->      </div>
    </div>
</a></li>
  </ul>
</div>
</ul>
</div>


</div>

            <footer class="course-player__branding-badge _branding-badge_qlbigq">
    <a href="http://www.thinkific.com/?ref=lms1stopai-poweredby" rel="noreferrer noopener" target="_blank" class="course-player__branding-badge__link _branding-badge__link_qlbigq _branding-badge__link--with-padding_qlbigq" data-ember-action="" data-ember-action-1580="1580">
      <svg role="img" width="203px" height="9px" viewBox="0 0 203 9" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <title>Teach online with Thinkific</title>
        <g id="Components" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
          <g id="4-Under-review-Copy-41" transform="translate(-77.000000, -771.000000)" fill="#3D4E5D" fill-rule="nonzero">
            <g id="Group-6" transform="translate(77.000000, 771.000000)">
              <path d="M6.072,0.1 C6.1120002,0.1 6.14599986,0.11399986 6.174,0.142 C6.20200014,0.17000014 6.216,0.2039998 6.216,0.244 L6.216,0.52 C6.216,0.5600002 6.20200014,0.59399986 6.174,0.622 C6.14599986,0.65000014 6.1120002,0.664 6.072,0.664 L3.696,0.664 C3.66399984,0.664 3.648,0.67999984 3.648,0.712 L3.648,8.356 C3.648,8.3960002 3.63400014,8.42999986 3.606,8.458 C3.57799986,8.48600014 3.5440002,8.5 3.504,8.5 L3.156,8.5 C3.1159998,8.5 3.08200014,8.48600014 3.054,8.458 C3.02599986,8.42999986 3.012,8.3960002 3.012,8.356 L3.012,0.712 C3.012,0.67999984 2.99600016,0.664 2.964,0.664 L0.708,0.664 C0.6679998,0.664 0.63400014,0.65000014 0.606,0.622 C0.57799986,0.59399986 0.564,0.5600002 0.564,0.52 L0.564,0.244 C0.564,0.2039998 0.57799986,0.17000014 0.606,0.142 C0.63400014,0.11399986 0.6679998,0.1 0.708,0.1 L6.072,0.1 Z M14.356,0.52 C14.356,0.5600002 14.3420001,0.59399986 14.314,0.622 C14.2859999,0.65000014 14.2520002,0.664 14.212,0.664 L9.688,0.664 C9.65599984,0.664 9.64,0.67999984 9.64,0.712 L9.64,3.952 C9.64,3.98400016 9.65599984,4 9.688,4 L12.892,4 C12.9320002,4 12.9659999,4.01399986 12.994,4.042 C13.0220001,4.07000014 13.036,4.1039998 13.036,4.144 L13.036,4.42 C13.036,4.4600002 13.0220001,4.49399986 12.994,4.522 C12.9659999,4.55000014 12.9320002,4.564 12.892,4.564 L9.688,4.564 C9.65599984,4.564 9.64,4.57999984 9.64,4.612 L9.64,7.888 C9.64,7.92000016 9.65599984,7.936 9.688,7.936 L14.212,7.936 C14.2520002,7.936 14.2859999,7.94999986 14.314,7.978 C14.3420001,8.00600014 14.356,8.0399998 14.356,8.08 L14.356,8.356 C14.356,8.3960002 14.3420001,8.42999986 14.314,8.458 C14.2859999,8.48600014 14.2520002,8.5 14.212,8.5 L9.148,8.5 C9.1079998,8.5 9.07400014,8.48600014 9.046,8.458 C9.01799986,8.42999986 9.004,8.3960002 9.004,8.356 L9.004,0.244 C9.004,0.2039998 9.01799986,0.17000014 9.046,0.142 C9.07400014,0.11399986 9.1079998,0.1 9.148,0.1 L14.212,0.1 C14.2520002,0.1 14.2859999,0.11399986 14.314,0.142 C14.3420001,0.17000014 14.356,0.2039998 14.356,0.244 L14.356,0.52 Z M22.244,8.5 C22.1639996,8.5 22.1120001,8.4600004 22.088,8.38 L21.572,6.808 C21.564,6.78399988 21.5480001,6.772 21.524,6.772 L17.78,6.772 C17.7559999,6.772 17.74,6.78399988 17.732,6.808 L17.228,8.38 C17.2039999,8.4600004 17.1520004,8.5 17.072,8.5 L16.688,8.5 C16.6399998,8.5 16.6040001,8.48600014 16.58,8.458 C16.5559999,8.42999986 16.5519999,8.38800028 16.568,8.332 L19.232,0.22 C19.2560001,0.1399996 19.3079996,0.1 19.388,0.1 L19.904,0.1 C19.9840004,0.1 20.0359999,0.1399996 20.06,0.22 L22.736,8.332 C22.744,8.34800008 22.748,8.36799988 22.748,8.392 C22.748,8.46400036 22.7040004,8.5 22.616,8.5 L22.244,8.5 Z M17.924,6.184 C17.916,6.20000008 17.9179999,6.21399994 17.93,6.226 C17.9420001,6.23800006 17.9559999,6.244 17.972,6.244 L21.332,6.244 C21.3480001,6.244 21.3619999,6.23800006 21.374,6.226 C21.3860001,6.21399994 21.388,6.20000008 21.38,6.184 L19.676,0.928 C19.668,0.91199992 19.6560001,0.904 19.64,0.904 C19.6239999,0.904 19.612,0.91199992 19.604,0.928 L17.924,6.184 Z M27.78,8.608 C27.2359973,8.608 26.7560021,8.50000108 26.34,8.284 C25.9239979,8.06799892 25.6020011,7.76200198 25.374,7.366 C25.1459989,6.96999802 25.032,6.51600256 25.032,6.004 L25.032,2.584 C25.032,2.07199744 25.1459989,1.62200194 25.374,1.234 C25.6020011,0.84599806 25.9239979,0.54400108 26.34,0.328 C26.7560021,0.11199892 27.2359973,0.004 27.78,0.004 C28.3160027,0.004 28.7919979,0.10999894 29.208,0.322 C29.6240021,0.53400106 29.9459989,0.83199808 30.174,1.216 C30.4020011,1.60000192 30.516,2.04399748 30.516,2.548 C30.516,2.5880002 30.5020001,2.62199986 30.474,2.65 C30.4459999,2.67800014 30.4120002,2.692 30.372,2.692 L30.024,2.704 C29.9279995,2.704 29.88,2.68000024 29.88,2.632 L29.88,2.56 C29.88,1.959997 29.6880019,1.47800182 29.304,1.114 C28.9199981,0.74999818 28.4120032,0.568 27.78,0.568 C27.1399968,0.568 26.6280019,0.74999818 26.244,1.114 C25.8599981,1.47800182 25.668,1.959997 25.668,2.56 L25.668,6.04 C25.668,6.640003 25.8619981,7.12399816 26.25,7.492 C26.6380019,7.86000184 27.1479968,8.044 27.78,8.044 C28.4120032,8.044 28.9199981,7.86000184 29.304,7.492 C29.6880019,7.12399816 29.88,6.640003 29.88,6.04 C29.88,5.95199956 29.9279995,5.908 30.024,5.908 L30.372,5.92 C30.4680005,5.92 30.516,5.9399998 30.516,5.98 L30.516,6.04 C30.516,6.54400252 30.4020011,6.98999806 30.174,7.378 C29.9459989,7.76600194 29.6240021,8.06799892 29.208,8.284 C28.7919979,8.50000108 28.3160027,8.608 27.78,8.608 Z M38.452,0.244 C38.452,0.2039998 38.4659999,0.17000014 38.494,0.142 C38.5220001,0.11399986 38.5559998,0.1 38.596,0.1 L38.944,0.1 C38.9840002,0.1 39.0179999,0.11399986 39.046,0.142 C39.0740001,0.17000014 39.088,0.2039998 39.088,0.244 L39.088,8.356 C39.088,8.3960002 39.0740001,8.42999986 39.046,8.458 C39.0179999,8.48600014 38.9840002,8.5 38.944,8.5 L38.596,8.5 C38.5559998,8.5 38.5220001,8.48600014 38.494,8.458 C38.4659999,8.42999986 38.452,8.3960002 38.452,8.356 L38.452,4.612 C38.452,4.57999984 38.4360002,4.564 38.404,4.564 L34.276,4.564 C34.2439998,4.564 34.228,4.57999984 34.228,4.612 L34.228,8.356 C34.228,8.3960002 34.2140001,8.42999986 34.186,8.458 C34.1579999,8.48600014 34.1240002,8.5 34.084,8.5 L33.736,8.5 C33.6959998,8.5 33.6620001,8.48600014 33.634,8.458 C33.6059999,8.42999986 33.592,8.3960002 33.592,8.356 L33.592,0.244 C33.592,0.2039998 33.6059999,0.17000014 33.634,0.142 C33.6620001,0.11399986 33.6959998,0.1 33.736,0.1 L34.084,0.1 C34.1240002,0.1 34.1579999,0.11399986 34.186,0.142 C34.2140001,0.17000014 34.228,0.2039998 34.228,0.244 L34.228,3.952 C34.228,3.98400016 34.2439998,4 34.276,4 L38.404,4 C38.4360002,4 38.452,3.98400016 38.452,3.952 L38.452,0.244 Z M48.42,8.596 C47.8679972,8.596 47.3820021,8.48200114 46.962,8.254 C46.5419979,8.02599886 46.2180011,7.70600206 45.99,7.294 C45.7619989,6.88199794 45.648,6.40800268 45.648,5.872 L45.648,2.728 C45.648,2.19199732 45.7619989,1.71800206 45.99,1.306 C46.2180011,0.89399794 46.5419979,0.57400114 46.962,0.346 C47.3820021,0.11799886 47.8679972,0.004 48.42,0.004 C48.9720028,0.004 49.4599979,0.11799886 49.884,0.346 C50.3080021,0.57400114 50.6359988,0.89399794 50.868,1.306 C51.1000012,1.71800206 51.216,2.19199732 51.216,2.728 L51.216,5.872 C51.216,6.40800268 51.1000012,6.88199794 50.868,7.294 C50.6359988,7.70600206 50.3080021,8.02599886 49.884,8.254 C49.4599979,8.48200114 48.9720028,8.596 48.42,8.596 Z M48.42,8.044 C49.0680032,8.044 49.589998,7.84800196 49.986,7.456 C50.382002,7.06399804 50.58,6.54400324 50.58,5.896 L50.58,2.716 C50.58,2.0759968 50.382002,1.55800198 49.986,1.162 C49.589998,0.76599802 49.0680032,0.568 48.42,0.568 C47.7799968,0.568 47.264002,0.76599802 46.872,1.162 C46.479998,1.55800198 46.284,2.0759968 46.284,2.716 L46.284,5.896 C46.284,6.54400324 46.479998,7.06399804 46.872,7.456 C47.264002,7.84800196 47.7799968,8.044 48.42,8.044 Z M54.532,8.5 C54.4919998,8.5 54.4580001,8.48600014 54.43,8.458 C54.4019999,8.42999986 54.388,8.3960002 54.388,8.356 L54.388,0.244 C54.388,0.2039998 54.4019999,0.17000014 54.43,0.142 C54.4580001,0.11399986 54.4919998,0.1 54.532,0.1 L54.892,0.1 C54.9720004,0.1 55.0279998,0.13199968 55.06,0.196 L59.368,7.18 C59.376,7.20400012 59.388,7.21400002 59.404,7.21 C59.4200001,7.20599998 59.428,7.19200012 59.428,7.168 L59.428,0.244 C59.428,0.2039998 59.4419999,0.17000014 59.47,0.142 C59.4980001,0.11399986 59.5319998,0.1 59.572,0.1 L59.92,0.1 C59.9600002,0.1 59.9939999,0.11399986 60.022,0.142 C60.0500001,0.17000014 60.064,0.2039998 60.064,0.244 L60.064,8.356 C60.064,8.3960002 60.0500001,8.42999986 60.022,8.458 C59.9939999,8.48600014 59.9600002,8.5 59.92,8.5 L59.56,8.5 C59.4799996,8.5 59.4240002,8.46800032 59.392,8.404 L55.084,1.408 C55.076,1.38399988 55.0640001,1.37399998 55.048,1.378 C55.0319999,1.38200002 55.024,1.39599988 55.024,1.42 L55.024,8.356 C55.024,8.3960002 55.0100001,8.42999986 54.982,8.458 C54.9539999,8.48600014 54.9200002,8.5 54.88,8.5 L54.532,8.5 Z M63.656,8.5 C63.6159998,8.5 63.5820001,8.48600014 63.554,8.458 C63.5259999,8.42999986 63.512,8.3960002 63.512,8.356 L63.512,0.244 C63.512,0.2039998 63.5259999,0.17000014 63.554,0.142 C63.5820001,0.11399986 63.6159998,0.1 63.656,0.1 L64.004,0.1 C64.0440002,0.1 64.0779999,0.11399986 64.106,0.142 C64.1340001,0.17000014 64.148,0.2039998 64.148,0.244 L64.148,7.888 C64.148,7.92000016 64.1639998,7.936 64.196,7.936 L68.48,7.936 C68.5200002,7.936 68.5539999,7.94999986 68.582,7.978 C68.6100001,8.00600014 68.624,8.0399998 68.624,8.08 L68.624,8.356 C68.624,8.3960002 68.6100001,8.42999986 68.582,8.458 C68.5539999,8.48600014 68.5200002,8.5 68.48,8.5 L63.656,8.5 Z M71.46,8.5 C71.4199998,8.5 71.3860001,8.48600014 71.358,8.458 C71.3299999,8.42999986 71.316,8.3960002 71.316,8.356 L71.316,0.244 C71.316,0.2039998 71.3299999,0.17000014 71.358,0.142 C71.3860001,0.11399986 71.4199998,0.1 71.46,0.1 L71.808,0.1 C71.8480002,0.1 71.8819999,0.11399986 71.91,0.142 C71.9380001,0.17000014 71.952,0.2039998 71.952,0.244 L71.952,8.356 C71.952,8.3960002 71.9380001,8.42999986 71.91,8.458 C71.8819999,8.48600014 71.8480002,8.5 71.808,8.5 L71.46,8.5 Z M75.556,8.5 C75.5159998,8.5 75.4820001,8.48600014 75.454,8.458 C75.4259999,8.42999986 75.412,8.3960002 75.412,8.356 L75.412,0.244 C75.412,0.2039998 75.4259999,0.17000014 75.454,0.142 C75.4820001,0.11399986 75.5159998,0.1 75.556,0.1 L75.916,0.1 C75.9960004,0.1 76.0519998,0.13199968 76.084,0.196 L80.392,7.18 C80.4,7.20400012 80.412,7.21400002 80.428,7.21 C80.4440001,7.20599998 80.452,7.19200012 80.452,7.168 L80.452,0.244 C80.452,0.2039998 80.4659999,0.17000014 80.494,0.142 C80.5220001,0.11399986 80.5559998,0.1 80.596,0.1 L80.944,0.1 C80.9840002,0.1 81.0179999,0.11399986 81.046,0.142 C81.0740001,0.17000014 81.088,0.2039998 81.088,0.244 L81.088,8.356 C81.088,8.3960002 81.0740001,8.42999986 81.046,8.458 C81.0179999,8.48600014 80.9840002,8.5 80.944,8.5 L80.584,8.5 C80.5039996,8.5 80.4480002,8.46800032 80.416,8.404 L76.108,1.408 C76.1,1.38399988 76.0880001,1.37399998 76.072,1.378 C76.0559999,1.38200002 76.048,1.39599988 76.048,1.42 L76.048,8.356 C76.048,8.3960002 76.0340001,8.42999986 76.006,8.458 C75.9779999,8.48600014 75.9440002,8.5 75.904,8.5 L75.556,8.5 Z M89.696,0.52 C89.696,0.5600002 89.6820001,0.59399986 89.654,0.622 C89.6259999,0.65000014 89.5920002,0.664 89.552,0.664 L85.028,0.664 C84.9959998,0.664 84.98,0.67999984 84.98,0.712 L84.98,3.952 C84.98,3.98400016 84.9959998,4 85.028,4 L88.232,4 C88.2720002,4 88.3059999,4.01399986 88.334,4.042 C88.3620001,4.07000014 88.376,4.1039998 88.376,4.144 L88.376,4.42 C88.376,4.4600002 88.3620001,4.49399986 88.334,4.522 C88.3059999,4.55000014 88.2720002,4.564 88.232,4.564 L85.028,4.564 C84.9959998,4.564 84.98,4.57999984 84.98,4.612 L84.98,7.888 C84.98,7.92000016 84.9959998,7.936 85.028,7.936 L89.552,7.936 C89.5920002,7.936 89.6259999,7.94999986 89.654,7.978 C89.6820001,8.00600014 89.696,8.0399998 89.696,8.08 L89.696,8.356 C89.696,8.3960002 89.6820001,8.42999986 89.654,8.458 C89.6259999,8.48600014 89.5920002,8.5 89.552,8.5 L84.488,8.5 C84.4479998,8.5 84.4140001,8.48600014 84.386,8.458 C84.3579999,8.42999986 84.344,8.3960002 84.344,8.356 L84.344,0.244 C84.344,0.2039998 84.3579999,0.17000014 84.386,0.142 C84.4140001,0.11399986 84.4479998,0.1 84.488,0.1 L89.552,0.1 C89.5920002,0.1 89.6259999,0.11399986 89.654,0.142 C89.6820001,0.17000014 89.696,0.2039998 89.696,0.244 L89.696,0.52 Z M97.684,8.5 C97.5959996,8.5 97.5400001,8.4600004 97.516,8.38 L95.188,0.256 L95.176,0.208 C95.176,0.13599964 95.2199996,0.1 95.308,0.1 L95.68,0.1 C95.7680004,0.1 95.8239999,0.1399996 95.848,0.22 L97.828,7.192 C97.836,7.20800008 97.8459999,7.216 97.858,7.216 C97.8700001,7.216 97.88,7.20800008 97.888,7.192 L99.712,0.22 C99.7360001,0.1399996 99.7919996,0.1 99.88,0.1 L100.264,0.1 C100.352,0.1 100.408,0.1399996 100.432,0.22 L102.328,7.192 C102.336,7.20800008 102.346,7.216 102.358,7.216 C102.37,7.216 102.38,7.20800008 102.388,7.192 L104.38,0.22 C104.404,0.1399996 104.46,0.1 104.548,0.1 L104.896,0.1 C105.000001,0.1 105.04,0.15199948 105.016,0.256 L102.688,8.38 C102.664,8.4600004 102.608,8.5 102.52,8.5 L102.148,8.5 C102.06,8.5 102.004,8.4600004 101.98,8.38 L100.108,1.276 C100.1,1.25999992 100.092,1.252 100.084,1.252 C100.076,1.252 100.068,1.25999992 100.06,1.276 L98.2,8.38 C98.176,8.4600004 98.1200004,8.5 98.032,8.5 L97.684,8.5 Z M107.72,8.5 C107.68,8.5 107.646,8.48600014 107.618,8.458 C107.59,8.42999986 107.576,8.3960002 107.576,8.356 L107.576,0.244 C107.576,0.2039998 107.59,0.17000014 107.618,0.142 C107.646,0.11399986 107.68,0.1 107.72,0.1 L108.068,0.1 C108.108,0.1 108.142,0.11399986 108.17,0.142 C108.198,0.17000014 108.212,0.2039998 108.212,0.244 L108.212,8.356 C108.212,8.3960002 108.198,8.42999986 108.17,8.458 C108.142,8.48600014 108.108,8.5 108.068,8.5 L107.72,8.5 Z M116.52,0.1 C116.56,0.1 116.594,0.11399986 116.622,0.142 C116.65,0.17000014 116.664,0.2039998 116.664,0.244 L116.664,0.52 C116.664,0.5600002 116.65,0.59399986 116.622,0.622 C116.594,0.65000014 116.56,0.664 116.52,0.664 L114.144,0.664 C114.112,0.664 114.096,0.67999984 114.096,0.712 L114.096,8.356 C114.096,8.3960002 114.082,8.42999986 114.054,8.458 C114.026,8.48600014 113.992,8.5 113.952,8.5 L113.604,8.5 C113.564,8.5 113.53,8.48600014 113.502,8.458 C113.474,8.42999986 113.46,8.3960002 113.46,8.356 L113.46,0.712 C113.46,0.67999984 113.444,0.664 113.412,0.664 L111.156,0.664 C111.116,0.664 111.082,0.65000014 111.054,0.622 C111.026,0.59399986 111.012,0.5600002 111.012,0.52 L111.012,0.244 C111.012,0.2039998 111.026,0.17000014 111.054,0.142 C111.082,0.11399986 111.116,0.1 111.156,0.1 L116.52,0.1 Z M124.312,0.244 C124.312,0.2039998 124.326,0.17000014 124.354,0.142 C124.382,0.11399986 124.416,0.1 124.456,0.1 L124.804,0.1 C124.844,0.1 124.878,0.11399986 124.906,0.142 C124.934,0.17000014 124.948,0.2039998 124.948,0.244 L124.948,8.356 C124.948,8.3960002 124.934,8.42999986 124.906,8.458 C124.878,8.48600014 124.844,8.5 124.804,8.5 L124.456,8.5 C124.416,8.5 124.382,8.48600014 124.354,8.458 C124.326,8.42999986 124.312,8.3960002 124.312,8.356 L124.312,4.612 C124.312,4.57999984 124.296,4.564 124.264,4.564 L120.136,4.564 C120.104,4.564 120.088,4.57999984 120.088,4.612 L120.088,8.356 C120.088,8.3960002 120.074,8.42999986 120.046,8.458 C120.018,8.48600014 119.984,8.5 119.944,8.5 L119.596,8.5 C119.556,8.5 119.522,8.48600014 119.494,8.458 C119.466,8.42999986 119.452,8.3960002 119.452,8.356 L119.452,0.244 C119.452,0.2039998 119.466,0.17000014 119.494,0.142 C119.522,0.11399986 119.556,0.1 119.596,0.1 L119.944,0.1 C119.984,0.1 120.018,0.11399986 120.046,0.142 C120.074,0.17000014 120.088,0.2039998 120.088,0.244 L120.088,3.952 C120.088,3.98400016 120.104,4 120.136,4 L124.264,4 C124.296,4 124.312,3.98400016 124.312,3.952 L124.312,0.244 Z" id="TEACHONLINEWITH"></path>
              <g id="Group-5" transform="translate(132.000000, 0.250000)">
                <path d="M5.63671712,0.0259471718 L0.473837,0.0259471718 C0.212144051,0.0259471718 3.55271368e-14,0.242359715 3.55271368e-14,0.509318116 L3.55271368e-14,0.509318116 C3.55271368e-14,0.776276517 0.212144051,0.99268906 0.473837,0.99268906 L2.50819712,0.99268906 L2.50819712,7.38782389 C2.50819649,7.51588205 2.55816611,7.63867315 2.64707102,7.72908078 C2.73597592,7.81948842 2.85650238,7.87007525 2.98203412,7.86967242 L3.11805673,7.86967242 C3.24358847,7.87007525 3.36411493,7.81948842 3.45301983,7.72908078 C3.54192474,7.63867315 3.59189436,7.51588205 3.59189373,7.38782389 L3.59189373,0.99268906 L5.63671712,0.99268906 C5.89841007,0.99268906 6.11055413,0.776276517 6.11055413,0.509318116 L6.11055413,0.509318116 C6.11055413,0.242359715 5.89841007,0.0259471718 5.63671712,0.0259471718 L5.63671712,0.0259471718 Z" id="Shape"></path>
                <path d="M15.904182,7.32530588 L15.904182,0.579460272 C15.904182,0.274357922 15.6621645,0.0267876742 15.363081,0.0259471718 L15.363081,0.0259471718 C15.0637545,0.0267848972 14.8213066,0.274111098 14.8204854,0.579460272 L14.8204854,3.54677843 L10.3526658,3.54677843 L10.3526658,0.579460272 C10.352667,0.274357922 10.1106483,0.0267876742 9.81156489,0.0259471718 L9.81156489,0.0259471718 C9.51248147,0.0267876742 9.27046396,0.274357922 9.27046396,0.579460272 L9.27046396,7.32530588 C9.27046396,7.47170227 9.32747265,7.61210264 9.42894876,7.71562053 C9.53042487,7.81913841 9.668056,7.87729415 9.81156489,7.87729415 L9.81156489,7.87729415 C9.95507378,7.87729415 10.0927049,7.81913841 10.194181,7.71562053 C10.2956571,7.61210264 10.3526658,7.47170227 10.3526658,7.32530588 L10.3526658,4.51199549 L14.8204854,4.51199549 L14.8204854,7.32530588 C14.8213093,7.63040707 15.0639965,7.87729415 15.363081,7.87729415 L15.363081,7.87729415 C15.5065899,7.87729415 15.6442211,7.81913841 15.7456972,7.71562053 C15.8471733,7.61210264 15.904182,7.47170227 15.904182,7.32530588 L15.904182,7.32530588 Z" id="Shape"></path>
                <path d="M20.545393,0.0259471718 C20.8442348,0.0259471718 21.0864939,0.268206309 21.0864939,0.5670481 L21.0864939,7.32856907 C21.0864939,7.62741086 20.8442348,7.86967 20.545393,7.86967 C20.2465512,7.86967 20.004292,7.62741086 20.004292,7.32856907 L20.004292,0.5670481 C20.004292,0.268206309 20.2465512,0.0259471718 20.545393,0.0259471718 Z" id="Rectangle-path"></path>
                <path d="M31.8218167,7.10725526 L31.8218167,0.567261636 C31.8218167,0.268896385 31.585153,0.0267876373 31.2926738,0.0259471718 L31.2926738,0.0259471718 C30.9996107,0.0259471718 30.7620362,0.268301913 30.7620362,0.567261636 L30.7620362,6.11459127 L26.5363668,0.333962726 C26.3952214,0.14198224 26.1737076,0.0289968308 25.9384652,0.0289968308 L25.9384652,0.0289968308 C25.5257003,0.0289968308 25.1910882,0.370341536 25.1910882,0.791411569 L25.1910882,7.32530588 C25.1910882,7.46873157 25.2470416,7.60626077 25.3465987,7.70753491 C25.4461558,7.80880905 25.5811297,7.86550067 25.7217259,7.86509551 L25.7441472,7.86509551 C26.0358008,7.86425505 26.2717965,7.62282899 26.2717953,7.32530588 L26.2717953,1.79169971 L30.4735487,7.56317927 C30.6146941,7.75515976 30.8362079,7.86815128 31.0714502,7.86815128 L31.0714502,7.86815128 C31.2699256,7.86895545 31.4605659,7.78919699 31.6013304,7.64645845 C31.7420948,7.50371991 31.8214214,7.30972535 31.8218167,7.10725526 L31.8218167,7.10725526 Z" id="Shape"></path>
                <path d="M36.4749858,0.0259471718 C36.7738275,0.0259471718 37.0160867,0.268206309 37.0160867,0.5670481 L37.0160867,7.32856907 C37.0160867,7.62741086 36.7738275,7.86967 36.4749858,7.86967 C36.176144,7.86967 35.9338848,7.62741086 35.9338848,7.32856907 L35.9338848,0.5670481 C35.9338848,0.268206309 36.176144,0.0259471718 36.4749858,0.0259471718 Z" id="Rectangle-path"></path>
                <path d="M41.2659373,7.86967339 L41.3212432,7.86967339 C41.5082993,7.8703738 41.6791351,7.76145422 41.7604849,7.58962311 C41.8418347,7.41779199 41.8192456,7.21357744 41.7024054,7.06456004 L39.1418919,3.78007734 L41.4707186,0.835631624 C41.5887229,0.686786608 41.6124572,0.482042566 41.5317408,0.309225058 C41.4510243,0.136407551 41.2802009,0.0262275812 41.0925458,0.0259471718 L41.0925458,0.0259471718 C40.9494107,0.0285443835 40.8145383,0.0948308085 40.7233416,0.20740188 L38.2465343,3.2707843 C37.9827792,3.59821689 37.9827792,4.07020069 38.2465343,4.39763328 L40.8922488,7.68821529 C40.9836599,7.80303266 41.1209404,7.86967339 41.2659373,7.86967339 Z" id="Shape"></path>
                <path d="M46.3807201,0.0259471718 C46.6795619,0.0259471718 46.9218211,0.268206309 46.9218211,0.5670481 L46.9218211,7.32856907 C46.9218211,7.62741086 46.6795619,7.86967 46.3807201,7.86967 C46.0818784,7.86967 45.8396192,7.62741086 45.8396192,7.32856907 L45.8396192,0.5670481 C45.8396192,0.268206309 46.0818784,0.0259471718 46.3807201,0.0259471718 Z" id="Rectangle-path"></path>
                <path d="M55.2490953,3.59252332 L52.110112,3.59252332 L52.110112,0.99268906 L55.6317523,0.99268906 C55.888402,0.992701086 56.0971504,0.781793573 56.0996318,0.519991922 L56.0996318,0.507793286 C56.1008071,0.38042225 56.0520439,0.25784784 55.9641734,0.167350226 C55.876303,0.0768526125 55.7566168,0.0259471718 55.6317523,0.0259471718 L51.5017472,0.0259471718 C51.2375776,0.0259471718 51.0234259,0.244407783 51.0234259,0.513892604 L51.0234259,7.3939232 C51.0242496,7.65691736 51.2334757,7.86967 51.4912839,7.86967 L51.6407593,7.86967 C51.8985675,7.86967 52.1077936,7.65691736 52.1086173,7.3939232 L52.1086173,4.54706657 L55.2476005,4.54706657 C55.5042385,4.54455717 55.7109861,4.33160862 55.7109743,4.06979494 L55.7109743,4.06979494 C55.7109952,3.80856878 55.5051482,3.59586167 55.2490953,3.59252332 Z" id="Shape"></path>
                <path d="M59.8469584,0.0259471718 C60.1458002,0.0259471718 60.3880594,0.268206309 60.3880594,0.5670481 L60.3880594,7.32856907 C60.3880594,7.62741086 60.1458002,7.86967 59.8469584,7.86967 C59.5481166,7.86967 59.3058575,7.62741086 59.3058575,7.32856907 L59.3058575,0.5670481 C59.3058575,0.268206309 59.5481166,0.0259471718 59.8469584,0.0259471718 Z" id="Rectangle-path"></path>
                <path d="M63.8319724,3.93713478 C63.8319724,6.17558445 65.5912978,7.93523767 67.8364183,7.93523767 C68.7408572,7.91903973 69.6173493,7.612817 70.3416259,7.05998555 C70.4464254,6.97807486 70.5128369,6.85515934 70.5247641,6.72103001 C70.5366914,6.58690068 70.4930457,6.4538007 70.4044055,6.3539895 L70.4044055,6.3539895 C70.2423283,6.17198986 69.9721425,6.14311515 69.7766089,6.286897 C69.2298083,6.68759862 68.5767949,6.90982667 67.9036822,6.92427572 C66.2872948,6.92427572 64.976954,5.58756986 64.976954,3.93865961 C64.976954,2.28974936 66.2872948,0.953043494 67.9036822,0.953043494 C68.5795017,0.965096983 69.2335712,1.19873433 69.7691351,1.61939397 C69.9727612,1.77059028 70.257071,1.73088775 70.4133741,1.52942904 L70.4328059,1.50503176 C70.5138043,1.40371514 70.5508178,1.27309445 70.5353035,1.14331774 C70.5197893,1.01354103 70.4530879,0.895822996 70.3505944,0.81733367 C69.6298049,0.291635468 68.7673002,0.00616068437 67.8812609,-2.11386464e-13 C65.6107296,-0.00759907667 63.8319724,1.72460721 63.8319724,3.93713478 Z" id="Shape"></path>
              </g>
            </g>
          </g>
        </g>
      </svg>
      <span class="sr-only">Opens in a new window</span>
    </a>
  </footer>

        </nav>

        <main id="main-content" tabindex="-1" class="course-player__lesson _course-player__lesson_n1vbpj">
<section class="surface__container _surface__container_1yatsw _surface--content_1yatsw">
              <div class="_content-surface_n1vbpj">
                <div class="course-player__content-header _content-header__container_h7ytgy">
  <div class="_content-header__title-container_h7ytgy">
        <h2 class="course-player__content-header__title _content-header__title_h7ytgy">IRIS -MODEL.IPYNB</h2>
  </div>
  <div class="course-player__content-header__actions _content-header__actions_h7ytgy">
<!----><!---->
    <button class="course-player__content-header__action-fullscreen _content-header__action-fullscreen_h7ytgy" data-ember-action="" data-ember-action-1596="1596">
        <span class="sr-only">Enable fullscreen</span>
        <i aria-hidden="true" class="toga-icon toga-icon-arrow-grow"></i>
    </button>
  </div>
</div>


              <div class="content-modal-wrapper _content-modal-wrapper_n1vbpj">
                <div class="content-modal _content-modal_n1vbpj">
<!---->
<!---->
                  <section id="content-inner" class="course-player__content-inner _content-inner_n1vbpj">
<!---->
                    
                    <div class="course-player__html-item _html-item__container_1vr68b">
  <div id="ember2183" class="ember-view"><!----></div>

  <div id="ember2184" class="ember-view"><div class="custom-theme">
  <div class="fr-view">
    <div class="fr-view"><p>{<br>"cells": [<br>{<br>"cell_type": "markdown",<br>"metadata": {},<br>"source": [<br>"# &nbsp;Iris class prediction "<br>]<br>},<br>{<br>"cell_type": "code",<br>"execution_count": 10,<br>"metadata": {},<br>"outputs": [<br>{<br>"name": "stdout",<br>"output_type": "stream",<br>"text": [<br>"pandas version is: 0.24.2\n",<br>"numpy version is:1.16.2\n"<br>]<br>}<br>],<br>"source": [<br>"import pandas &nbsp; &nbsp;\n",<br>"print('pandas version is: {}'.format(pandas.__version__)) &nbsp; &nbsp;\n",<br>"import numpy &nbsp; &nbsp;\n",<br>"print('numpy version is:{}'.format(numpy.__version__)) &nbsp; &nbsp;\n",<br>"import seaborn as sns &nbsp; &nbsp; &nbsp;\n",<br>"import sklearn &nbsp; &nbsp; &nbsp;\n",<br>"import matplotlib.pyplot as plt\n",<br>"%matplotlib inline"<br>]<br>},<br>{<br>"cell_type": "markdown",<br>"metadata": {},<br>"source": [<br>"### Importing data set "<br>]<br>},<br>{<br>"cell_type": "code",<br>"execution_count": 2,<br>"metadata": {},<br>"outputs": [],<br>"source": [<br>"import pandas as pd &nbsp;\n",<br>"iris=pd.read_csv('iris_csv.csv') &nbsp;"<br>]<br>},<br>{<br>"cell_type": "code",<br>"execution_count": 4,<br>"metadata": {},<br>"outputs": [<br>{<br>"data": {<br>"text/html": [<br>"&lt;div&gt;\n",<br>"&lt;style scoped&gt;\n",<br>" &nbsp; &nbsp;.dataframe tbody tr th:only-of-type {\n",<br>" &nbsp; &nbsp; &nbsp; &nbsp;vertical-align: middle;\n",<br>" &nbsp; &nbsp;}\n",<br>"\n",<br>" &nbsp; &nbsp;.dataframe tbody tr th {\n",<br>" &nbsp; &nbsp; &nbsp; &nbsp;vertical-align: top;\n",<br>" &nbsp; &nbsp;}\n",<br>"\n",<br>" &nbsp; &nbsp;.dataframe thead th {\n",<br>" &nbsp; &nbsp; &nbsp; &nbsp;text-align: right;\n",<br>" &nbsp; &nbsp;}\n",<br>"&lt;/style&gt;\n",<br>"&lt;table border=\"1\" class=\"dataframe\"&gt;\n",<br>" &nbsp;&lt;thead&gt;\n",<br>" &nbsp; &nbsp;&lt;tr style=\"text-align: right;\"&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;th&gt;&lt;/th&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;th&gt;sepallength&lt;/th&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;th&gt;sepalwidth&lt;/th&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;th&gt;petallength&lt;/th&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;th&gt;petalwidth&lt;/th&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;th&gt;class&lt;/th&gt;\n",<br>" &nbsp; &nbsp;&lt;/tr&gt;\n",<br>" &nbsp;&lt;/thead&gt;\n",<br>" &nbsp;&lt;tbody&gt;\n",<br>" &nbsp; &nbsp;&lt;tr&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;th&gt;0&lt;/th&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;5.1&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;3.5&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;1.4&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;0.2&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;Iris-setosa&lt;/td&gt;\n",<br>" &nbsp; &nbsp;&lt;/tr&gt;\n",<br>" &nbsp; &nbsp;&lt;tr&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;th&gt;1&lt;/th&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;4.9&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;3.0&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;1.4&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;0.2&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;Iris-setosa&lt;/td&gt;\n",<br>" &nbsp; &nbsp;&lt;/tr&gt;\n",<br>" &nbsp; &nbsp;&lt;tr&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;th&gt;2&lt;/th&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;4.7&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;3.2&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;1.3&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;0.2&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;Iris-setosa&lt;/td&gt;\n",<br>" &nbsp; &nbsp;&lt;/tr&gt;\n",<br>" &nbsp; &nbsp;&lt;tr&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;th&gt;3&lt;/th&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;4.6&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;3.1&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;1.5&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;0.2&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;Iris-setosa&lt;/td&gt;\n",<br>" &nbsp; &nbsp;&lt;/tr&gt;\n",<br>" &nbsp; &nbsp;&lt;tr&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;th&gt;4&lt;/th&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;5.0&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;3.6&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;1.4&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;0.2&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;Iris-setosa&lt;/td&gt;\n",<br>" &nbsp; &nbsp;&lt;/tr&gt;\n",<br>" &nbsp; &nbsp;&lt;tr&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;th&gt;5&lt;/th&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;5.4&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;3.9&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;1.7&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;0.4&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;Iris-setosa&lt;/td&gt;\n",<br>" &nbsp; &nbsp;&lt;/tr&gt;\n",<br>" &nbsp; &nbsp;&lt;tr&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;th&gt;6&lt;/th&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;4.6&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;3.4&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;1.4&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;0.3&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;Iris-setosa&lt;/td&gt;\n",<br>" &nbsp; &nbsp;&lt;/tr&gt;\n",<br>" &nbsp; &nbsp;&lt;tr&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;th&gt;7&lt;/th&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;5.0&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;3.4&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;1.5&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;0.2&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;Iris-setosa&lt;/td&gt;\n",<br>" &nbsp; &nbsp;&lt;/tr&gt;\n",<br>" &nbsp; &nbsp;&lt;tr&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;th&gt;8&lt;/th&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;4.4&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;2.9&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;1.4&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;0.2&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;Iris-setosa&lt;/td&gt;\n",<br>" &nbsp; &nbsp;&lt;/tr&gt;\n",<br>" &nbsp; &nbsp;&lt;tr&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;th&gt;9&lt;/th&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;4.9&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;3.1&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;1.5&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;0.1&lt;/td&gt;\n",<br>" &nbsp; &nbsp; &nbsp;&lt;td&gt;Iris-setosa&lt;/td&gt;\n",<br>" &nbsp; &nbsp;&lt;/tr&gt;\n",<br>" &nbsp;&lt;/tbody&gt;\n",<br>"&lt;/table&gt;\n",<br>"&lt;/div&gt;"<br>],<br>"text/plain": [<br>" &nbsp; sepallength &nbsp;sepalwidth &nbsp;petallength &nbsp;petalwidth &nbsp; &nbsp; &nbsp; &nbsp;class\n",<br>"0 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;5.1 &nbsp; &nbsp; &nbsp; &nbsp; 3.5 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;1.4 &nbsp; &nbsp; &nbsp; &nbsp; 0.2 &nbsp;Iris-setosa\n",<br>"1 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;4.9 &nbsp; &nbsp; &nbsp; &nbsp; 3.0 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;1.4 &nbsp; &nbsp; &nbsp; &nbsp; 0.2 &nbsp;Iris-setosa\n",<br>"2 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;4.7 &nbsp; &nbsp; &nbsp; &nbsp; 3.2 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;1.3 &nbsp; &nbsp; &nbsp; &nbsp; 0.2 &nbsp;Iris-setosa\n",<br>"3 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;4.6 &nbsp; &nbsp; &nbsp; &nbsp; 3.1 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;1.5 &nbsp; &nbsp; &nbsp; &nbsp; 0.2 &nbsp;Iris-setosa\n",<br>"4 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;5.0 &nbsp; &nbsp; &nbsp; &nbsp; 3.6 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;1.4 &nbsp; &nbsp; &nbsp; &nbsp; 0.2 &nbsp;Iris-setosa\n",<br>"5 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;5.4 &nbsp; &nbsp; &nbsp; &nbsp; 3.9 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;1.7 &nbsp; &nbsp; &nbsp; &nbsp; 0.4 &nbsp;Iris-setosa\n",<br>"6 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;4.6 &nbsp; &nbsp; &nbsp; &nbsp; 3.4 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;1.4 &nbsp; &nbsp; &nbsp; &nbsp; 0.3 &nbsp;Iris-setosa\n",<br>"7 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;5.0 &nbsp; &nbsp; &nbsp; &nbsp; 3.4 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;1.5 &nbsp; &nbsp; &nbsp; &nbsp; 0.2 &nbsp;Iris-setosa\n",<br>"8 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;4.4 &nbsp; &nbsp; &nbsp; &nbsp; 2.9 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;1.4 &nbsp; &nbsp; &nbsp; &nbsp; 0.2 &nbsp;Iris-setosa\n",<br>"9 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;4.9 &nbsp; &nbsp; &nbsp; &nbsp; 3.1 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;1.5 &nbsp; &nbsp; &nbsp; &nbsp; 0.1 &nbsp;Iris-setosa"<br>]<br>},<br>"execution_count": 4,<br>"metadata": {},<br>"output_type": "execute_result"<br>}<br>],<br>"source": [<br>"iris.head(10)"<br>]<br>},<br>{<br>"cell_type": "markdown",<br>"metadata": {},<br>"source": [<br>"### analyse and visualize data set "<br>]<br>},<br>{<br>"cell_type": "code",<br>"execution_count": 6,<br>"metadata": {},<br>"outputs": [<br>{<br>"name": "stdout",<br>"output_type": "stream",<br>"text": [<br>"150\n"<br>]<br>}<br>],<br>"source": [<br>"print(len(iris['class']))"<br>]<br>},<br>{<br>"cell_type": "code",<br>"execution_count": 7,<br>"metadata": {},<br>"outputs": [<br>{<br>"name": "stdout",<br>"output_type": "stream",<br>"text": [<br>"sepallength\n",<br>"sepalwidth\n",<br>"petallength\n",<br>"petalwidth\n",<br>"class\n"<br>]<br>}<br>],<br>"source": [<br>"for col in iris.columns:\n",<br>" &nbsp; &nbsp;print(col)"<br>]<br>},<br>{<br>"cell_type": "code",<br>"execution_count": 8,<br>"metadata": {},<br>"outputs": [<br>{<br>"name": "stdout",<br>"output_type": "stream",<br>"text": [<br>"class\n",<br>"Iris-setosa &nbsp; &nbsp; &nbsp; &nbsp;50\n",<br>"Iris-versicolor &nbsp; &nbsp;50\n",<br>"Iris-virginica &nbsp; &nbsp; 50\n",<br>"dtype: int64\n"<br>]<br>}<br>],<br>"source": [<br>"print(iris.groupby('class').size()) "<br>]<br>},<br>{<br>"cell_type": "code",<br>"execution_count": 11,<br>"metadata": {},<br>"outputs": [<br>{<br>"data": {<br>"text/plain": [<br>"&lt;matplotlib.axes._subplots.AxesSubplot at 0x21789c832b0&gt;"<br>]<br>},<br>"execution_count": 11,<br>"metadata": {},<br>"output_type": "execute_result"<br>},<br>{<br>"data": {<br>"image/png": "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\n",<br>"text/plain": [<br>"&lt;Figure size 1080x720 with 4 Axes&gt;"<br>]<br>},<br>"metadata": {<br>"needs_background": "light"<br>},<br>"output_type": "display_data"<br>}<br>],<br>"source": [<br>"plt.figure(figsize=(15,10)) &nbsp; &nbsp;\n",<br>"plt.subplot(2,2,1) &nbsp; &nbsp;\n",<br>"sns.boxplot(x='class',y='sepallength',data=iris) &nbsp; &nbsp;\n",<br>"plt.subplot(2,2,2) &nbsp; &nbsp;\n",<br>"sns.boxplot(x='class',y='sepalwidth',data=iris) &nbsp; &nbsp;\n",<br>"plt.subplot(2,2,3) &nbsp; &nbsp;\n",<br>"sns.boxplot(x='class',y='petallength',data=iris) &nbsp; &nbsp;\n",<br>"plt.subplot(2,2,4) &nbsp; &nbsp;\n",<br>"sns.boxplot(x='class',y='petalwidth',data=iris) &nbsp; &nbsp;"<br>]<br>},<br>{<br>"cell_type": "code",<br>"execution_count": null,<br>"metadata": {},<br>"outputs": [],<br>"source": [<br>"# data cleaning "<br>]<br>},<br>{<br>"cell_type": "code",<br>"execution_count": 12,<br>"metadata": {},<br>"outputs": [<br>{<br>"data": {<br>"text/plain": [<br>"False"<br>]<br>},<br>"execution_count": 12,<br>"metadata": {},<br>"output_type": "execute_result"<br>}<br>],<br>"source": [<br>"iris.isnull().values.any()"<br>]<br>},<br>{<br>"cell_type": "code",<br>"execution_count": 13,<br>"metadata": {},<br>"outputs": [<br>{<br>"name": "stdout",<br>"output_type": "stream",<br>"text": [<br>"&lt;class 'pandas.core.frame.DataFrame'&gt;\n",<br>"RangeIndex: 150 entries, 0 to 149\n",<br>"Data columns (total 5 columns):\n",<br>"sepallength &nbsp; &nbsp;150 non-null float64\n",<br>"sepalwidth &nbsp; &nbsp; 150 non-null float64\n",<br>"petallength &nbsp; &nbsp;150 non-null float64\n",<br>"petalwidth &nbsp; &nbsp; 150 non-null float64\n",<br>"class &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;150 non-null object\n",<br>"dtypes: float64(4), object(1)\n",<br>"memory usage: 5.9+ KB\n"<br>]<br>}<br>],<br>"source": [<br>"iris.info()"<br>]<br>},<br>{<br>"cell_type": "markdown",<br>"metadata": {},<br>"source": [<br>"### splitting up of data "<br>]<br>},<br>{<br>"cell_type": "code",<br>"execution_count": 14,<br>"metadata": {},<br>"outputs": [],<br>"source": [<br>"from sklearn.model_selection import train_test_split\n",<br>"array = iris.values &nbsp; &nbsp;\n",<br>"X = array[:,0:4] &nbsp; &nbsp;\n",<br>"Y = array[:,4] &nbsp; &nbsp; &nbsp;\n",<br>"x_train,x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3,random_state=0) &nbsp; &nbsp;\n"<br>]<br>},<br>{<br>"cell_type": "markdown",<br>"metadata": {},<br>"source": [<br>"### Apply algorithms and evaluate "<br>]<br>},<br>{<br>"cell_type": "markdown",<br>"metadata": {},<br>"source": [<br>"## SUPPORT VECTOR CLASSIFIER "<br>]<br>},<br>{<br>"cell_type": "code",<br>"execution_count": 18,<br>"metadata": {},<br>"outputs": [<br>{<br>"name": "stdout",<br>"output_type": "stream",<br>"text": [<br>"Accuracy : 98.0\n"<br>]<br>}<br>],<br>"source": [<br>"from sklearn.svm import SVC\n",<br>"from sklearn.metrics import accuracy_score\n",<br>"svc = SVC(max_iter=1000,gamma='auto')\n",<br>"svc.fit(x_train, y_train)\n",<br>"y_pred = svc.predict(x_test)\n",<br>"acc_svc = round(accuracy_score(y_pred,y_test) , 2)*100\n",<br>"print(\"Accuracy :\" ,acc_svc)"<br>]<br>},<br>{<br>"cell_type": "markdown",<br>"metadata": {},<br>"source": [<br>"## DECISION TREE CLASSIFIER &nbsp;"<br>]<br>},<br>{<br>"cell_type": "code",<br>"execution_count": 19,<br>"metadata": {},<br>"outputs": [<br>{<br>"name": "stdout",<br>"output_type": "stream",<br>"text": [<br>"Accuracy : 98.0\n"<br>]<br>}<br>],<br>"source": [<br>"from sklearn.tree import DecisionTreeClassifier\n",<br>"\n",<br>"decisiontree = DecisionTreeClassifier( random_state=0)\n",<br>"decisiontree.fit(x_train, y_train)\n",<br>"y_pred = decisiontree.predict(x_test)\n",<br>"acc_decisiontree = round(accuracy_score(y_pred, y_test) , 2)*100\n",<br>"print(\"Accuracy :\" ,acc_decisiontree)"<br>]<br>},<br>{<br>"cell_type": "markdown",<br>"metadata": {},<br>"source": [<br>"## LOGISTIC REGRESSION "<br>]<br>},<br>{<br>"cell_type": "code",<br>"execution_count": 17,<br>"metadata": {},<br>"outputs": [<br>{<br>"name": "stdout",<br>"output_type": "stream",<br>"text": [<br>"Accuracy : &nbsp;89.0\n"<br>]<br>},<br>{<br>"name": "stderr",<br>"output_type": "stream",<br>"text": [<br>"C:\\Users\\JAHNAVI\\Anaconda3\\lib\\site-packages\\sklearn\\linear_model\\logistic.py:433: FutureWarning: Default solver will be changed to 'lbfgs' in 0.22. Specify a solver to silence this warning.\n",<br>" &nbsp;FutureWarning)\n",<br>"C:\\Users\\JAHNAVI\\Anaconda3\\lib\\site-packages\\sklearn\\linear_model\\logistic.py:460: FutureWarning: Default multi_class will be changed to 'auto' in 0.22. Specify the multi_class option to silence this warning.\n",<br>" &nbsp;\"this warning.\", FutureWarning)\n"<br>]<br>}<br>],<br>"source": [<br>"from sklearn.linear_model import LogisticRegression\n",<br>"logreg=LogisticRegression(max_iter=1000)\n",<br>"logreg.fit(x_train, y_train)\n",<br>"y_pred = logreg.predict(x_test)\n",<br>"acc_logreg = round(accuracy_score(y_pred, y_test) , 2)*100\n",<br>"print(\"Accuracy : \",acc_logreg)"<br>]<br>},<br>{<br>"cell_type": "markdown",<br>"metadata": {},<br>"source": [<br>"# &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; -------XXXX------"<br>]<br>},<br>{<br>"cell_type": "code",<br>"execution_count": null,<br>"metadata": {},<br>"outputs": [],<br>"source": []<br>}<br>],<br>"metadata": {<br>"kernelspec": {<br>"display_name": "Python 3",<br>"language": "python",<br>"name": "python3"<br>},<br>"language_info": {<br>"codemirror_mode": {<br>"name": "ipython",<br>"version": 3<br>},<br>"file_extension": ".py",<br>"mimetype": "text/x-python",<br>"name": "python",<br>"nbconvert_exporter": "python",<br>"pygments_lexer": "ipython3",<br>"version": "3.7.3"<br>}<br>},<br>"nbformat": 4,<br>"nbformat_minor": 2<br>}<br><br></p></div>
  </div>
</div></div>
</div>

                  </section>
                    <footer id="course-player-footer" data-navigation="content" aria-label="Course content navigation" class="course-player__content-navigation _content-navigation_apmbd3 _no-audio_apmbd3">
<!---->
        <div class="btn--incomplete _btn--incomplete_apmbd3">
  <button class="brand-color__border-60-opacity _button--ghost--small_142a8m" data-ember-action="" data-ember-action-2186="2186">
    <div class="_content__wrapper_142a8m">
<!---->  <div class="_content__container_142a8m">
                <span>Mark Incomplete</span>

  </div>
</div>

  </button>
        </div>

      <div class="btn--continue _btn--continue_apmbd3">
  <button class="brand-color__background brand-color__dynamic-text _button--default--small_142a8m _button--icon-right--small_142a8m" data-ember-action="" data-ember-action-2192="2192">
    <div class="_content__wrapper_142a8m">
<!---->  <div class="_content__container_142a8m">
              <span>Continue</span>
          <i aria-hidden="true" class="toga-icon toga-icon-arrow-right"></i>

  </div>
</div>

  </button>
      </div>
</footer>
<!---->
                </div>
              </div>
            </div>

</section>
        </main>

        <aside class="course-player__right-drawer _right-drawer_n1vbpj">
          <div class="course-player__course-discussions _course-discussions_n1vbpj">
            <!---->
          </div>
        </aside>

      </div>
<!---->  </div>

  <!---->
<!---->
<!---->  <div id="ember473" class="ember-notify-cn ember-notify-default ember-view"><!----></div>
</div></div></div>
<div id="push"></div>
</div>
<script src="./iris_files/vendor-4d6e9185450966c0cabdb0b6ab7efd2c.js.download"></script>
<script src="./iris_files/course-player-v2-c9365a5eaafcb1fceba95a2e1d99f0e4.js.download"></script>
<script src="./iris_files/kobayashi-9807c3a2da62e08d2b54c432bec5fb841b1cb7b22119b4b5f8773c1757d0c9f3.js.download"></script>
<script src="./iris_files/moment.min.js.download"></script>
<script src="./iris_files/jquery-ui.min.js.download"></script>
<script src="./iris_files/filestack.min.js.download"></script>
<script>
  $(function() { window.filestack = filestack.init('AJlfu1IB1Q9mpicgMdkVzz') });
</script>


<script>
  var userId = 40777349;
  var email = 'nehadubet@gmail.com';
  var mixpanelPerson = {
    $email: email,
    $created: '2021-03-03 08:44:23 +0000',
    $last_login: '2021-03-17 15:55:38 +0000',
    $first_name: 'Neha',
    $last_name: 'Dubey',
    'sign_in_count': 12,
    'admin': false,
    'referral_code': '',
    'tenant': 'Support\'s School',
    'subdomain': 'lms1stopai',
    'Is Paying': 'false',
    'Revenue': '0.0',
    'Courses': ["Machine Learning _E Learning  \u0026 Project_Beat The Virus"]
  };
  var personTraits = {
    'email': email,
    'createdAt': '2021-03-03T08:44:23+00:00',
    'firstName': 'Neha',
    'lastName': 'Dubey',
    'name': 'Neha Dubey'
  };
  ThinkificAnalytics.identify_for_tenant(email, mixpanelPerson, personTraits);
  ThinkificAnalytics.name_tag(email);
</script>







<script src="./iris_files/picker.js.download" id="__filestack-picker-module"></script></body></html>