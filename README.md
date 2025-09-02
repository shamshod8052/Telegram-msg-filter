# Telegram-msg-filter

Telegram xabarlarini filtrlash uchun loyiha.

---

## 🚀 Loyihani ishga tushirish

1. **Virtual environment yaratish**

   ```bash
   python -m venv venv
   ```

2. **Kerakli kutubxonalarni o‘rnatish**

   ```bash
   pip install -r requirements.txt
   ```

3. **.env faylni sozlash**
   `.env.example` fayliga qarab `.env` faylini yarating va o‘z ma’lumotlaringiz bilan to‘ldiring.

4. **Filterlarni belgilash**
   Loyihaning root papkasida `channels.json` faylini yarating va quyidagicha to‘ldiring:

   ```json
   [
     {
       "chat_id": "@OnlyPythonJobs",
       "parts_of_text": ["python"]
     }
   ]
   ```
