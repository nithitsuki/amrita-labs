import csv
import math
import sys

def get_grade(score, mean, std):
    ns = (score - mean) / std if std != 0 else 0
    if ns > 1.5: return 'O'
    elif ns > 1.0: return 'A+'
    elif ns > 0.5: return 'A'
    elif ns > 0.0: return 'B+'
    elif ns > -0.5: return 'B'
    elif ns > -1.0: return 'C'
    elif ns > -1.5: return 'D'
    else: return 'F'

def next_grade(grade):
    grades = ['F', 'D', 'C', 'B', 'B+', 'A', 'A+', 'O']
    if grade in grades and grade != 'O':
        return grades[grades.index(grade) + 1]
    return None

def grade_threshold(grade, mean, std):
    if grade == 'O': return mean + 1.5 * std
    elif grade == 'A+': return mean + 1.0 * std
    elif grade == 'A': return mean + 0.5 * std
    elif grade == 'B+': return mean + 0.0 * std
    elif grade == 'B': return mean - 0.5 * std
    elif grade == 'C': return mean - 1.0 * std
    elif grade == 'D': return mean - 1.5 * std
    else: return 0

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze.py <roll_number>")
        sys.exit(1)
        
    target_roll = sys.argv[1].upper()
    
    scores = []
    user_score = None
    
    with open('DAA_internals.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                score = float(row['Total-NO-FINAL-ROUNDED(70)'])
                scores.append(score)
                if row['RollNo'].strip().upper() == target_roll:
                    user_score = score
            except ValueError:
                continue

    if user_score is None:
        print(f"Roll number {target_roll} not found.")
        sys.exit(1)
        
    n = len(scores)
    mean = sum(scores) / n
    variance = sum((x - mean) ** 2 for x in scores) / n
    std = math.sqrt(variance)
    
    # Percentile
    scores.sort()
    rank = scores.index(user_score) # 0-indexed, handles duplicates essentially by finding first, but it's an estimate
    # For a better percentile calculation
    below = sum(1 for s in scores if s < user_score)
    percentile = (below / n) * 100
    
    current_grade = get_grade(user_score, mean, std)
    
    print("=== CURRENT STATUS (Out of 70) ===")
    print(f"Your Score: {user_score} / 70")
    print(f"Class Mean: {mean:.2f}, Std Dev: {std:.2f}")
    print(f"Your Percentile: {percentile:.1f}%")
    print(f"Your Current Grade: {current_grade}")
    
    print("\n=== PREDICTIONS FOR FINAL (Out of 100) ===")
    # Estimate total course mean and std based on proportionality
    estimated_total_mean = mean * (100 / 70)
    estimated_total_std = std * (100 / 70)
    
    print(f"Assuming final exam stats match current class performance distribution...")
    print(f"Estimated Final Mean (100): {estimated_total_mean:.2f}, Std Dev: {estimated_total_std:.2f}")
    
    req_maintain = grade_threshold(current_grade, estimated_total_mean, estimated_total_std)
    req_maintain_exam = req_maintain - user_score
    req_maintain_out_of_50 = (req_maintain_exam / 30) * 50
    
    print(f"\nTo MAINTAIN '{current_grade}' grade:")
    if req_maintain_out_of_50 <= 0:
        print(f"  You are guaranteed a {current_grade} (Need <= 0).")
    elif req_maintain_out_of_50 > 50:
        print(f"  It might not be mathematically possible to keep {current_grade} unless the class underperforms. (Need {req_maintain_out_of_50:.2f}/50)")
    else:
        print(f"  Need {req_maintain_exam:.2f}/30 scaled -> {req_maintain_out_of_50:.2f}/50 in the exam.")
        
    next_up = next_grade(current_grade)
    if next_up:
        req_improve = grade_threshold(next_up, estimated_total_mean, estimated_total_std)
        req_improve_exam = req_improve - user_score
        req_improve_out_of_50 = (req_improve_exam / 30) * 50
        print(f"\nTo IMPROVE to '{next_up}' grade:")
        if req_improve_out_of_50 > 50:
            print(f"  Probably impossible (Need {req_improve_out_of_50:.2f}/50, which is >50).")
        else:
            print(f"  Need {req_improve_exam:.2f}/30 scaled -> {req_improve_out_of_50:.2f}/50 in the exam.")

if __name__ == "__main__":
    main()
