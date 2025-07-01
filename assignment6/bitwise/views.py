from django.shortcuts import render
from .forms import NumberForm
from .models import CalculationResult

def calculate_view(request):
    result = None
    warning = None

    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            nums = [
                form.cleaned_data['a'],
                form.cleaned_data['b'],
                form.cleaned_data['c'],
                form.cleaned_data['d'],
                form.cleaned_data['e'],
            ]

            # Check for negative values
            negative_values = [n for n in nums if n < 0]
            if negative_values:
                warning = f"Warning: Negative values entered: {negative_values}"

            # Calculate average
            avg = sum(nums) / len(nums)
            avg_above_50 = avg > 50

            # Count positives
            positive_count = len([n for n in nums if n > 0])

            # Bitwise even/odd
            even_or_odd = []
            for n in nums:
                if n & 1 == 0:
                    even_or_odd.append(f"{n} is even (bitwise)")
                else:
                    even_or_odd.append(f"{n} is odd (bitwise)")

            # Values > 10, sorted
            greater_than_10 = [n for n in nums if n > 10]
            sorted_list = sorted(greater_than_10)

            # Save result to MongoDB
            CalculationResult.objects.create(
                a=nums[0],
                b=nums[1],
                c=nums[2],
                d=nums[3],
                e=nums[4],
                average=avg,
                avg_above_50=avg_above_50,
                positive_count=positive_count,
                even_or_odd_bitwise=", ".join(even_or_odd),
                original_list=nums,
                sorted_list=sorted_list,
            )

            result = {
                'original_list': nums,
                'average': avg,
                'avg_above_50': avg_above_50,
                'positive_count': positive_count,
                'even_or_odd_bitwise': even_or_odd,
                'sorted_list': sorted_list,
            }
    else:
        form = NumberForm()

    return render(request, 'Bitwise/calculate.html', {
        'form': form,
        'result': result,
        'warning': warning,
    })

