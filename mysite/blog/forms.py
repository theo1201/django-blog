from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    # 字段验证也依赖字段类型。例如，email 和 to 字段为 EmailField ，
    # 两个字段都需要有效地 e-mail 地址，否则字段验证将引发 forms.ValidationError 异常并且表单无法通过验证。
    email = forms.EmailField()
    to = forms.EmailField()
    # 。每一个字段都有默认的组件，这个组件决定 HTML 如何展示该字段。可以设置字段的 widget 属性覆盖默认的组件
    # 在 comments 字段中，我们使用 Textarea 组件表示使用<textarea> HTML元素代替默认的 <input> 元素
    comments = forms.CharField(required=False, widget=forms.Textarea)


