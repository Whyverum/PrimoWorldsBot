from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from BotLibrary import *

# Настройка роутера
router = Router(name="anketa_router")

# Определение состояния для работы с админом
class AdmAnswer(StatesGroup):
    waiting_for_message = State()  # Состояние ожидания сообщения от администратора

# Обработчик callback-запроса (нажатие на кнопку "Ответить пользователю")
@router.callback_query(lambda c: c.data.startswith("answer_user_"))
async def handle_respond_button(callback_query: types.CallbackQuery, state: FSMContext) -> None:
    # Извлекаем ID пользователя из callback_data
    user_id = int(callback_query.data.split("_")[2])

    # Сохраняем ID пользователя для дальнейшего использования
    await state.update_data(user_id=user_id)

    # Устанавливаем состояние для ожидания сообщения от администратора
    await state.set_state(AdmAnswer.waiting_for_message)

    # Отправляем админу запрос на ввод сообщения
    await callback_query.message.answer("Напишите сообщение, которое вы хотите отправить пользователю:")

    # Убираем кнопку из сообщения
    await callback_query.answer()

# Обработчик для получения сообщения от администратора и отправки его пользователю
@router.message(AdmAnswer.waiting_for_message)
async def handle_admin_message(message: types.Message, state: FSMContext) -> None:
    user_data = await state.get_data()
    user_id = user_data.get("user_id")

    if user_id:
        try:
            # Отправляем сообщение пользователю
            await bot.send_message(user_id, f"Администратор: {message.text}")

            # Подтверждаем админу, что сообщение отправлено
            await message.answer("Сообщение успешно отправлено пользователю.")
        except Exception as e:
            await message.answer(f"Произошла ошибка при отправке сообщения: {e}")
        finally:
            # Сбрасываем состояние
            await state.clear()
    else:
        # Если данные отсутствуют, информируем администратора
        await message.answer("Произошла ошибка. Попробуйте снова.")
