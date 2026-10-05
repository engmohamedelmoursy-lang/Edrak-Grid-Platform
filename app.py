# [الجزء الأول] كود الإصلاح البصري الجذري لقفل اتجاه السلايدرز طردياً - شركة RG ENERGY
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. الإعدادات القيادية للمنصة وتوسيع الشاشة بالكامل
st.set_page_config(page_title="RG ENERGY - Edrak Advanced Control", layout="wide", initial_sidebar_state="expanded")

# شفرة CSS المتقدمة والسحابية لقفل اتجاه السلايدرز طردياً مع الأرقام ومنع التداخل اللغوي
st.markdown("""
    <style>
    /* التنسيق العام المظلم والفاخر لغرف التحكم */
    .stApp { background-color: #060913 !important; color: #e6edf3 !important; font-family: sans-serif; }
    
    /* فرض المحاذاة العربية القياسية للمنصة من اليمين إلى اليسار للتبويبات والجداول */
    .stApp, div[data-testid='stTable'], .stTabs, div[role='tablist'], h1, h2, h3, p, li, div[data-testid='stMarkdownContainer'] {
        direction: RTL !important; text-align: right !important;
    }
    
    /* تنسيق القائمة الجانبية المظلمة */
    div[data-testid='stSidebar'] { 
        direction: RTL !important; text-align: right !important; 
        background-color: #0b0f19 !important; border-left: 1px solid #1f2937 !important; 
    }
    div[data-testid='stSidebar'] [data-testid='stMarkdownContainer'] p { color: #00ffcc !important; font-weight: bold !important; }
    
    /* 🛡️ القفل الهندسي المطلق: عزل السلايدر بالكامل وإجبار شريط السحب على التحرك طردياً من اليسار لليمين متزامناً مع الأرقام */
    div[data-testid='stSlider'] { 
        direction: LTR !important; 
        text-align: left !important;
        padding-left: 5px !important;
        padding-right: 5px !important;
    }
    
    /* تثبيت الأرقام والنطاقات بلون نيون فسفوري مضيء وموحد الاتجاه تصاعدياً */
    div[data-testid='stSlider'] span[data-baseweb='typography'] {
        color: #00ffcc !important;
        font-weight: bold !important;
        font-size: 15px !important;
        direction: LTR !important;
        display: inline-block !important;
        background-color: transparent !important;
    }
    
    /* تلوين أشرطة التمرير والمؤشرات لتتحرك بمرونة نيون احترافية مع القيمة زيادة ونقصاناً */
    div[data-testid='stSlider'] div[data-style] { background-color: #00ffcc !important; }
    div[data-testid='stSlider'] div[role='slider'] { background-color: #ffffff !important; border: 2px solid #00ffcc !important; box-shadow: 0 0 10px #00ffcc !important; }
    
    /* كروت المؤشرات الحيوية الفخمة */
    div[data-testid='stMetric'] {
        background-color: #0d1321 !important; border: 1px solid #1f2937 !important; border-radius: 12px !important;
        padding: 20px !important; box-shadow: 0 0 15px rgba(0, 255, 204, 0.15) !important;
    }
    th, td { text-align: right !important; direction: RTL !important; background-color: #0d1321 !important; color: #e6edf3 !important; border: 1px solid #1f2937 !important; }
    button[data-baseweb='tab'] { font-size: 16px !important; font-weight: bold !important; color: #8b949e !important; }
    button[aria-selected='true'] { color: #00ffcc !important; border-bottom-color: #00ffcc !important; }
    
    /* حاويات الأمن السيبراني عالية التباين والنصوع */
    .cyber-command-card {
        background: linear-gradient(135deg, #0d1321 0%, #111a2e 100%) !important;
        border-right: 4px solid #00ffcc !important; border-top: 1px solid #1f2937 !important;
        border-bottom: 1px solid #1f2937 !important; border-left: 1px solid #1f2937 !important;
        border-radius: 8px !important; padding: 20px !important; margin-bottom: 18px !important;
    }
    .cyber-card-title { color: #00ffcc !important; font-size: 18px !important; font-weight: bold !important; margin-bottom: 8px !important; }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 style="color: #00ffcc; text-shadow: 0 0 15px rgba(0,255,204,0.4); margin-bottom: 0;">⚡ إدراك | EDRAK</h1>', unsafe_allow_html=True)
st.markdown('<h3>نظام إدراكي تنبؤي ذاتي الشفاء لشبكات الكهرباء | RG ENERGY</h3>', unsafe_allow_html=True)
st.markdown('<hr style="border-color: #1f2937;">', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(['🎮 شاشة التوأم الرقمي والمحاكاة الحية', '📊 الجدوى والتحليل التنافسي والمالي', '🛡️ بروتوكولات الأمن السيبراني والمخاطر'])

with tab1:
    st.sidebar.header('🕹️ مركز التحكم والمناورة القيادي')
    simulation_mode = st.sidebar.selectbox('اختر حالة الشبكة للمحاكاة:', [
        'حالة تشغيل مستقرة آمنة',
        'افتعال عطل وقصر كهربائي مفاجئ',
        'دخول تدفق طاقة شمسية مفاجئ (Microgrid)'
    ])
    fault_select = st.sidebar.selectbox('حدد المحطة المستهدفة بالمعالجة الآلية:', [f'Sub_{i}' for i in range(1, 11)], index=4)
    
    # السلايدرز معزولة برمجياً لتبدأ تصاعدياً بطريقة صحيحة: الأقل في اليسار والأكبر في اليمين طردياً
    input_temp = st.sidebar.slider('قراءة مستشعرات الحرارة (°C):', min_value=50, max_value=120, value=72 if simulation_mode == 'حالة تشغيل مستقرة آمنة' else 105, step=1)
    input_load = st.sidebar.slider('نسبة الحمل الكهربائي على الباص (%):', min_value=40, max_value=110, value=60 if simulation_mode == 'حالة تشغيل مستقرة آمنة' else 96, step=1)
    
    is_fault_triggered = 0
    if simulation_mode == 'افتعال عطل وقصر كهربائي مفاجئ' or input_temp > 95 or input_load > 90:
        is_fault_triggered = 1
    
    col_m1, col_m2, col_m3 = st.columns(3)
    if simulation_mode == 'دخول تدفق طاقة شمسية مفاجئ (Microgrid)' and is_fault_triggered == 0:
        with col_m1: st.metric(label='🧠 مؤشر اتزان الشبكة (AI)', value='98%', delta='+3% (تكامل الطاقة النظيفة)', delta_color='normal')
        with col_m2: st.metric(label='📈 كفاءة تدفق الحمل (GAMS)', value='99.4%', delta='تشغيل نظام موازنة القدرة العكسية')
        with col_m3: st.metric(label='💡 إجمالي المفاقيد الكهربائية للخطوط', value='0.35%', delta='-0.17% (كفاءة قصوى بفضل GAMS)', delta_color='normal')
        st.warning(f'☀️ إنذار تشغيلي: تم رصد تدفق طاقة عكسي مفاجئ نتيجة توليد عالي من الخلايا الشمسية في المحطة ({fault_select})!')
        st.success('🟢 استجابة حاسمة مستقلة! استدعت منصة إدراك خوارزمية الأمثلة الرياضية في GAMS وضبطت اتزان التغذية اللامركزية في أقل من 15 ثانية.')
    elif is_fault_triggered == 1:
        with col_m1: st.metric(label='🧠 مؤشر صحة الشبكة الكلي (AI)', value='94%', delta='-6% (تراجع حرج)', delta_color='inverse')
        with col_m2: st.metric(label='📈 كفاءة تدفق الحمل (GAMS)', value='99.1%', delta='عزل آلي وموازنة التدفق')
        with col_m3: st.metric(label='💡 إجمالي المفاقيد الكهربائية للخطوط', value='0.90%', delta='+0.50% (ارتفاع حاد)', delta_color='inverse')
        st.error(f'🚨 إنذار استباقي فوري: تم رصد مؤشرات حرجة وقصر كهربائي (Short Circuit) في المحطة الفرعية ({fault_select})!')
        st.success('🟢 نجاح الشفاء الذاتي الآلي المستقل (Autonomous FLISR SUCCESS)! استجاب محرك GAMS 54 وعزل الخلل آلياً في أقل من 30 ثانية وبأدنى مفاقيد طاقة.')
    else:
        with col_m1: st.metric(label='🧠 مؤشر صحة الشبكة الكلي (AI)', value='100%', delta='مستقر وآمن', delta_color='normal')
        with col_m2: st.metric(label='📈 كفاءة تدفق الحمل (GAMS)', value='99.6%', delta='نطاق تشغيلي مثالي', delta_color='normal')
        with col_m3: st.metric(label='💡 إجمالي المفاقيد الكهربائية للخطوط', value='0.40%', delta='-0.12% تحسين مستمر', delta_color='normal')
        st.success('🟢 شبكة التوزيع آمنة وتعمل بكفاءة هندسية مطلقة؛ جميع خطوط التغذية والمحولات العشر تعمل ضمن النطاق الآمن.')
    st.markdown('<h3 style="color: #00ffcc;">🗺️ المخطط الهندسي لخطوط التغذية الحية ومسارات الشفاء الذاتي (Network Topology)</h3>', unsafe_allow_html=True)
    
    # الإحداثيات الجغرافية الموزعة هندسياً لـ 10 محطات لمنع التداخل البصري
    station_lat = [24.470, 24.478, 24.465, 24.482, 24.473, 24.458, 24.488, 24.479, 24.462, 24.469]
    station_lon = [39.610, 39.616, 39.605, 39.622, 39.629, 39.601, 39.613, 39.625, 39.632, 39.598]
    substations_list = [f'Sub_{i}' for i in range(1, 11)]
    
    fig_map, ax_map = plt.subplots(figsize=(11, 4.2))
    fig_map.patch.set_facecolor('#060913')
    ax_map.set_facecolor('#0d1321')
    ax_map.plot([39.595, 39.615, 39.635], [24.455, 24.473, 24.490], color='#1d2433', linewidth=4, alpha=0.4)
    
    # 1. رسم مسارات خطوط التغذية والربط الحلقي الملون
    for i in range(len(station_lat) - 1):
        if is_fault_triggered and (substations_list[i] == fault_select or substations_list[i+1] == fault_select):
            c = '#ff3333'; l_style = '--'; l_width = 3.0  # وميض أحمر يعكس العزل التلقائي للأعطال
        else:
            c = '#00ffcc'; l_style = '-'; l_width = 2.0   # أخضر نيون يعكس تدفق أمثلة GAMS المستقرة
        ax_map.plot([station_lon[i], station_lon[i+1]], [station_lat[i], station_lat[i+1]], color=c, linestyle=l_style, linewidth=l_width, zorder=3)
    
    # 2. إسقاط عقد المحطات العشر المضيئة حياً
    for i, name in enumerate(substations_list):
        if simulation_mode == 'دخول تدفق طاقة شمسية مفاجئ (Microgrid)' and name == fault_select and is_fault_triggered == 0:
            ax_map.scatter(station_lon[i], station_lat[i], color='#ff9800', s=160, zorder=5, edgecolors='white', linewidths=1.5)
            ax_map.text(station_lon[i], station_lat[i]+0.0012, f'☀️ {name}\\nطاقة متجددة حية', color='#ff9800', fontsize=8, fontweight='bold', ha='center')
        elif is_fault_triggered and name == fault_select:
            ax_map.scatter(station_lon[i], station_lat[i], color='#ff3333', s=160, zorder=5, edgecolors='white', linewidths=1.5)
            ax_map.text(station_lon[i], station_lat[i]+0.0012, f'🚨 {name}\\nمعزولة آلياً', color='#ff3333', fontsize=8, fontweight='bold', ha='center')
        else:
            ax_map.scatter(station_lon[i], station_lat[i], color='#ffeb3b', s=100, zorder=5, edgecolors='#060913', linewidths=1)
            ax_map.text(station_lon[i], station_lat[i]+0.0012, name, color='#c9d1d9', fontsize=8, ha='center')
            
    ax_map.axis('off')
    st.pyplot(fig_map)
    
    # رسم منحنى مستويات اتزان الجهد الكهربائي لعقد الشبكة
    st.write('### 📊 منحنى مستويات اتزان الجهد الكهربائي لعقد الشبكة (Voltage Profile Plot)')
    buses = [f'Node_{i}' for i in range(1, 11)]
    if is_fault_triggered:
        voltage_values = [1.00, 0.99, 0.97, 0.96, 0.955, 0.97, 0.98, 0.99, 0.98, 0.96]
    elif simulation_mode == 'دخول تدفق طاقة شمسية مفاجئ (Microgrid)':
        voltage_values = [1.02, 1.03, 1.01, 1.04, 1.02, 1.01, 1.01, 1.02, 1.01, 1.00]
    else:
        voltage_values = [1.00, 0.99, 0.99, 0.98, 0.985, 0.99, 0.99, 1.00, 0.99, 0.98]
    
    fig_v, ax_v = plt.subplots(figsize=(11, 2.5))
    fig_v.patch.set_facecolor('#060913')
    ax_v.set_facecolor('#0d1321')
    ax_v.plot(buses, voltage_values, marker='o', color='#00ffcc', linewidth=2.5)
    ax_v.axhline(y=1.05, color='#ff3333', linestyle='--', linewidth=1.2)
    ax_v.axhline(y=0.95, color='#ff9800', linestyle='--', linewidth=1.2)
    ax_v.set_ylim(0.90, 1.10)
    ax_v.grid(True, linestyle=':', alpha=0.1)
    st.pyplot(fig_v)
    
    status_list = ['🚨 FAULT / ISOLATED' if is_fault_triggered and s == fault_select else ('☀️ Renewable Active' if simulation_mode == 'دخول تدفق طاقة شمسية مفاجئ (Microgrid)' and s == fault_select else '🟢 Active') for s in substations_list]
    grid_map_data = {'اسم المحطة الفرعية': substations_list, 'الموقع الجغرافي': [f'القطاع {i}' for i in range(1, 11)], 'مستوى جهد التوزيع': ['11 kV'] * 10, 'الحالة التشغيلية حياً': status_list}
    st.table(pd.DataFrame(grid_map_data))

with tab2:
    st.write('## 📊 التحليل التنافسي والميزة الاحتكارية لـ RG ENERGY')
    competitor_matrix = {
        'الميزة الفنية والهندسية': ['طبيعة النظام والتشغيل', 'زمن عزل الأعطال وإعادة التغذية', 'آلية خفض مفاقيد الطاقة', 'إدارة الطاقة المتجددة اللامركزية'],
        'منصة إدراك (RG ENERGY) ⚡': [
            'إدراكي استباقي يتنبأ بالأعطال قبل حدوثها دون قيد زمني لمراقبة وتدفق النمط الحراري.',
            'أقل من 30 ثانية آلياً بالكامل بدون أي تدخل بشري لدقة النظم الميكانيكية.',
            'أمثلة رياضية صارمة غير خطية تختار المسار الأقل مقاومة بلحظات لتقليل مفاقيد الطاقة.',
            'مجهزة بالكامل لموازنة تدفق القدرة العكسي (Reverse Power) واستقرار الشبكات المصغرة.'
        ],
        'الأنظمة العالمية التقليدية (SCADA / DMS) 🏢': [
            'تفاعلي يستجيب فقط بعد وقوع العطل وانقطاع التيار فعلياً عن المشتركين.',
            'من دقائق إلى ساعات، ويتطلب نزول فرق صيانة ميدانية وتدخل يدوي من غرف التحكم.',
            'تعتمد على جداول توزيع ثابتة مسبقاً وتفتقر للمرونة التشغيلية اللحظية أثناء الطوارئ.',
            'تواجه صعوبة بالغة في موازنة الأحمال الشمسية المفاجئة وتتطلب تجهيزات فيزيائية مكلفة جداً.'
        ]
    }
    st.table(pd.DataFrame(competitor_matrix))
    st.write('## 💰 الهيكل الاقتصادي والنموذج المالي وعوائد الاستثمار لشركة RG ENERGY')
    col_cap, col_op = st.columns(2)
    with col_cap:
        st.write('### 🛠️ التكاليف الرأسمالية الأولية (CAPEX)')
        capex_data = {'بند الإنفاق التأسيسي للمنصة': ['تطوير البرمجيات (Python & GAMS)', 'أجهزة الـ PMUs وحساسات إنترنت الأشياء', 'الاستضافة السحابية الآمنة والسيرفرات'], 'التكلفة بالريال السعودي': ['200,000 ريال', '150,000 ريال', '50,000 ريال']}
        st.table(pd.DataFrame(capex_data))
    with col_op:
        st.write('### 📈 الوفر المالي ومصاريف التشغيل والصيانة (OPEX Savings)')
        st.write('• متوسط تكلفة الصيانة السنوية التقليدية للشبكة الكهربائية: 1,000,000 ريال.')
        st.write('• التكلفة التشغيلية الميدانية بعد تطبيق نظام إدراك (توفير 40%): 600,000 ريال.')
        st.success('💰 إجمالي الوفر المالي السنوي الصافي المحقق لمشغلي الشبكة: 400,000 ريال سعودي / سنوياً.')
    st.info('• **فترة استرداد رأس المال بالكامل (Payback Period):** سنة واحدة فقط.\\n• **العائد على الاستثمار المتوقع (Expected ROI) خلال 3 سنوات تشغيلية:** 200%.')

with tab3:
    st.write('## 🛡️ دليل الأمن السيبراني وإدارة المخاطر الفنية والخطط البديلة لـ منصة إدراك')
    st.write('لحماية المنظومة البرمجية المستقلة وضمان استمرارية التشغيل الميداني الآمن، تم تفعيل بروتوكولات الأمان التالية:')
    st.markdown('''
    <div class='cyber-command-card'>
        <div class='cyber-card-title'>🔒 1. جدار الحماية ضد الاختراق وحقن البيانات المفاجئ (Cyber Security)</div>
        <div class='cyber-command-card-text' style='color: #ffffff !important; line-height: 1.7; text-align: right;'>يتم تشفير قنوات اتصال الحساسات والـ PMUs بالكامل (End-to-End Encryption) لمنع التلاعب بالقراءات الحرارية، مع تفعيل بروتوكول التحقق الثنائي الفيزيائي اللحظي لمقارنة التنبؤ الحراري باتزان اتجاهات الطاقة في محرك GAMS.</div>
    </div>
    <div class='cyber-command-card'>
        <div class='cyber-card-title'>📡 2. خطة الاتصال البديل الفوري عند انقطاع الإشارة (Redundancy)</div>
        <div class='cyber-command-card-text' style='color: #ffffff !important; line-height: 1.7; text-align: right;'>في حال تعطل قنوات الألياف الضوئية أو الشبكات الخلوية الرئيسية نتيجة طقس حاد، تنتقل المنصة آلياً لشبكة بث لاسلكية احتياطية منخفضة الطاقة (LoRaWAN) أو الاتصال الفضائي للأقمار الصناعية لضمان تدفق البيانات التشغيلية الحيوية دون انقطاع.</div>
    </div>
    <div class='cyber-command-card'>
        <div class='cyber-card-title'>⚙️ 3. التحكم المحلي اللامركزي وقواطع الطوارئ (Edge Control Contingency)</div>
        <div class='cyber-command-card-text' style='color: #ffffff !important; line-height: 1.7; text-align: right;'>عند الانقطاع التام والكامل للاتصال بغرفة التحكم المركزية، تمتلك قواطع الشبكة الذكية (Reclosers) والمفاتيح الميدانية القدرة الذاتية على تشغيل خوارزميات العزل محلياً وعزل القصر الكهربائي (Short Circuit) حماية للمحولات المليونية والالتزام التام بضوابط الهيئة السعودية لتنظيم الكهرباء.</div>
    </div>
    ''', unsafe_allow_html=True)
