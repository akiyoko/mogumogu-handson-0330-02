from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import BookForm
from .models import Book


class BookIndexView(View):
    def get(self, request, *args, **kwargs):
        context = {
            # 本レコードの一覧を取得
            'book_list': Book.objects.all(),
        }
        # ショップ画面を表示
        return render(request, 'shop/book_list.html', context)


index = BookIndexView.as_view()


class BookCreateView(View):
    def get(self, request, *args, **kwargs):
        context = {
            # 空のフォームを作成
            'form': BookForm(),
        }
        # 登録画面を表示
        return render(request, 'shop/book_form.html', context)

    def post(self, request, *args, **kwargs):
        # リクエストの入力データをフォームオブジェクトに変換
        form = BookForm(request.POST)
        # バリデーション実行
        if not form.is_valid():
            context = {
                'form': form,
            }
            # 登録画面を再表示
            return render(request, 'shop/book_form.html', context)
        # モデルオブジェクトを保存
        form.save()
        # ショップ画面にリダイレクト
        return redirect('/shop/')


create = BookCreateView.as_view()
