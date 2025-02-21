#=========================================================================
# [AutoDelete - Telegram bot to delete messages after specific time]      
# Copyright (C) 2022 Arunkumar Shibu                       
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#=========================================================================

import os

API_ID       = int(os.environ.get("API_ID", "18674011"))
API_HASH     = os.environ.get("API_HASH", "38d3664512757d8830601169eff5a1de")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "7945022794:AAEdwZt7jCowhJ-ZO1QVQhRTG1OJV5kZ6Ag")
SESSION      = os.environ.get("SESSION", "")
TIME         = int(os.environ.get("TIME", 2))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1002251825993 -1002274439678 -1002262472330 -1001643696419 -1002130385569").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://C:C@cluster0.danekjk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
PORT         = os.environ.get("PORT", "8080")
